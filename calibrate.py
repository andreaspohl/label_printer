# calibrate a servo

from servo import Servo
from commons import Commons
import sys, tty
from time import sleep


if Commons.EMBEDDED:
    import PCA9685 as pca

def clip(servo, pos):
    return servo.clip_pulse(pos)

# deactive normalization
def de_norm(servo):
    servo.min = 0
    servo.max = 3000
    servo.min_pulse = 0
    servo.max_pulse = 3000
    servo.pos = 1500
    return 1500

axes = None
while axes not in ('x', 'y', 'pen'):
    axes = input('Enter servo axes to calibrate (x, y, pen):')

servo = Servo(axes)

pos = 500

hat = None
if Commons.EMBEDDED:
    hat = pca.PCA9685(0x40, debug=False)
    hat.setPWMFreq(50)

print('POSITION')
print('A/a: decrease by 10/1')
print('D/d: increase by 10/1')
print('-+: set to min/max position')
print()
print('PULSE')
print('n: deactivate normalization')
print('s: set to 1000 ns, S set to 2000ns')
print('q: quit')

go_on = True
normalized = True

while go_on:  # making a loop

    tty.setcbreak(sys.stdin)  
    key = sys.stdin.read(1)  # key captures the key-code 
    if key == 's' and not normalized:
        pos = 1000
    if key == 'S' and not normalized:
        pos = 2000
    elif key == 'A':
        pos = pos - 10
    elif key == 'a':
        pos = pos - 1
    elif key == 'd':
        pos = pos + 1
    elif key == 'D':
        pos = pos + 10
    elif key == 'n':
        normalized = False
        pos = de_norm(servo)
    elif key == '+' and normalized:
        pos = servo.max
    elif key == '-' and normalized:
        pos = servo.min
    elif key == 'q':
        go_on = False

    if normalized:
        pos = servo.clip(pos)
        servo.move(pos)
        print(f'pos = {pos}')
    else:
        pos = servo.clip_pulse(pos)
        servo.set_pwm(pos)
        print(f'pulse = {pos}')
