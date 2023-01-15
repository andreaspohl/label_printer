from commons import Commons as cm

if cm.EMBEDDED:
    from PCA9685 import PCA9685 

class Servo:
    axes = None
    min = 0 # value for lower limit
    max = 1000 # value for upper limit (for y axes)
    pos = 0 # actual position, also position at power up

    hat = None

    min_pulse = 1000 # pulse length (ns) value for left/lower pos, will be overwritten by calibrated value
    max_pulse = 2000 # pulse length (ns) value for right/upper pos, will be overwritten by calibrated value

    def __init__(self, axes = 'x') -> None:
        self.axes = 'x'
        if axes == 'x':
            self.min_pulse = cm.X_MIN_PULSE
            self.max_pulse = cm.X_MAX_PULSE
            self.channel = cm.X_SERVO_CHANNEL
            self.max = cm.X_MAX
        if axes == 'y':
            self.min_pulse = cm.Y_MIN_PULSE
            self.max_pulse = cm.Y_MAX_PULSE
            self.channel = cm.Y_SERVO_CHANNEL
        if axes == 'pen':
            self.min_pulse = cm.PEN_MIN_PULSE
            self.max_pulse = cm.PEN_MAX_PULSE
            self.channel = cm.PEN_SERVO_CHANNEL

        if cm.EMBEDDED:
            if self.hat is None:
                self.hat = PCA9685(0x40)
                self.hat.setPWMFreq(50)

    # limit pos to min/max values
    def clip(self, pos):
        return sorted([self.min, pos, self.max])[1]

    def clip_pulse(self, pulse):
        return sorted([self.min_pulse, pulse, self.max_pulse])[1]

    def info(self):
        print('min: ', self.min)
        print('max: ', self.max)
        print('pos: ', self.pos)

    # set servo to a new position, but does not move it yet
    def set(self, value = -1):
        if value != -1:
            self.pos = self.clip(value)

    # set server pwm pulse (only for calibration)
    def set_pwm(self, pulse):
        self.hat.setServoPulse(self.channel, pulse)
        # print(f'pulse: {pulse}')

    # move servo to previously set position (or to given position)
    def move(self, pos = None):
        if pos is not None:
            self.pos = self.clip(pos)
        self.pos = self.clip(self.pos)
        pulse = self.calc_pulse(self.pos)
        self.hat.setServoPulse(self.channel, pulse)
        # print(f'pulse: {pulse}')
    
    # calculate pwm pulse length
    def calc_pulse(self, pos = None):
        if pos == None:
            pos = self.pos 
        pulse = pos * (self.max_pulse - self.min_pulse) / (self.max - self.min) + self.min_pulse
        return pulse
    
    def inc(self, value = 1):
        self.pos += value
        self.pos = self.clip(self.pos)
    
    def decr(self, value = 1):
        self.pos -= value
        self.pos = self.clip(self.pos)