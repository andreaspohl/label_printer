# the tape 'canvas' is 1000 dots high and several 1000 dots wide

class Commons:

    EMBEDDED = True # set to true if run on RPI
    PEN_ARMED = False # set to False if pen must stay up all the time

    SPEED = 500 # pen speed is 500 dots per second, i.e. half the height of the canvas

    PERIOD = 20 # servo positions are set all 20 ms (50 Hz)

    CODE_UP = 'G0'
    CODE_DOWN = 'G1'

    X_MAX = 5333
    X_MIN_PULSE = 240
    X_MAX_PULSE = 2330

    Y_MIN_PULSE = 1300
    Y_MAX_PULSE = 1760

    PEN_MIN_PULSE = 1206
    PEN_MAX_PULSE = 1700

    PEN_SERVO_CHANNEL = 0
    X_SERVO_CHANNEL = 1
    Y_SERVO_CHANNEL = 2

    UP_DOWN_DURATION = 500 # time to move the pen up/down [ms]



