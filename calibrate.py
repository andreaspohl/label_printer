# calibrate a servo

from servo import Servo
from commons import Commons
import sys, tty
from time import sleep

def clip(servo, pos):
    return sorted([servo.min, pos, servo.max])[1]


axes = None
while axes not in ('x', 'y', 'pen'):
    axes = input('Enter servo axes to calibrate (x, y, pen):')

print('A/a decrease by 10/1, D/d increase by 10/1, s set to 1000 ns, S set to 2000ns, q quit')

servo = Servo(axes)

# deactive normalization
servo.min = 0
servo.max = 3000
servo.min_pulse = 0
servo.max_pulse = 3000
servo.pos = 1500
pos = 1500

go_on = True

while go_on:  # making a loop

    tty.setcbreak(sys.stdin)  
    key = sys.stdin.read(1)  # key captures the key-code 
    if key == 's':
        pos = 1000
    if key == 'S':
        pos = 2000
    elif key == 'A':
        pos = pos - 10
    elif key == 'a':
        pos = pos - 1
    elif key == 'd':
        pos = pos + 1
    elif key == 'D':
        pos = pos + 10
    elif key == 'q':
        go_on = False
    pos = clip(servo, pos)
    servo.set(pos)
    for i in range(0, 10):
        servo.move()
        sleep(Commons.PERIOD / 1000)
    print(pos)
