# the tape 'canvas' is 1000 dots high and several 1000 dots wide

class Commons:

    SPEED = 500 # pen speed is 500 dots per second, i.e. half the height of the canvas

    PERIOD = 20 # servo positions are set all 20 ms (50 Hz)

    CODE_UP = 'G0'
    CODE_DOWN = 'G1'

    X_MIN_PULSE = 1000
    X_MAX_PULSE = 2000

    Y_MIN_PULSE = 1000
    Y_MAX_PULSE = 2000

    PEN_MIN_PULSE = 1000
    PEN_MAX_PULSE = 2000

    UP_DOWN_DURATION = 500 # time to move the pen up/down [ms]



