# the tape 'canvas' is 1000 dots high and several 1000 dots wide

class Commons:

    EMBEDDED = True # set to true if run on RPI

    SPEED = 500 # pen speed is 500 dots per second, i.e. half the height of the canvas

    PERIOD = 20 # servo positions are set all 20 ms (50 Hz)

    CODE_UP = 'G0'
    CODE_DOWN = 'G1'

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

    # 50 dots top/bottom margin, 6.15 is single row max, -1.76 is single row min
    LINE_SPACING = 8.0
    SCALING_HANGING_SIZE = 1.76
    SCALING_FACTOR = 1 / (6.15 + LINE_SPACING + 1.76) * (1000 - 100) # factor to fit 2 lines
    SCALING_OFFSET = 50 # bottom margin



