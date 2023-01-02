from commons import Commons as cm

class Servo:
    axes = None
    min = 0 # value for left/lower limit
    max = 1000 # value for right/upper limit
    pos = 500 # actual position, also position at power up

    min_pulse = 1000 # pulse length (ns) value for left/lower pos, will be overwritten by calibrated value
    max_pulse = 2000 # pulse length (ns) value for right/upper pos, will be overwritten by calibrated value

    def __init__(self, axes = 'x') -> None:
        self.axes = 'x'
        if axes == 'x':
            self.min_pulse = cm.X_MIN_PULSE
            self.max_pulse = cm.X_MAX_PULSE
        if axes == 'y':
            self.min_pulse = cm.Y_MIN_PULSE
            self.max_pulse = cm.Y_MAX_PULSE
        if axes == 'pen':
            self.min_pulse = cm.PEN_MIN_PULSE
            self.max_pulse = cm.PEN_MAX_PULSE

    def clip(self, pos):
        return sorted([self.min, pos, self.max])[1]

    def info(self):
        print('min: ', self.min)
        print('max: ', self.max)
        print('pos: ', self.pos)

    def inc(self, value = 1):
        self.pos += value
        self.pos = self.clip(self.pos)
    
    def set(self, value = -1):
        if value != -1:
            self.pos = self.clip(value)

    def move(self):
        self.pos = self.clip(self.pos)
        # TODO: write to servo
        # print(f'servo: {self.axes} pos: {self.pos} pwm: {self.calc_pwm()}')
    
    def calc_pwm(self, pos = None):
        if pos == None:
            pos = self.pos 
        pwm = pos * (self.max_pulse - self.min_pulse) / 1000 + self.min_pulse
        return pwm
    
    def decr(self, value = 1):
        self.pos -= value
        self.pos = self.clip(self.pos)
    
    def set_lower_range_limit(self):
        self.min_pulse = self.calc_pwm()