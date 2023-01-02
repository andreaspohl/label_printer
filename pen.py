# this class is for positioning the pen on the tape
from servo import Servo
from command import Command as gp
import numpy as np
from commons import Commons as cm
from numpy import linalg as la
from time import sleep
import plot as pl

class Pen:

    debug = False

    number_of_steps = None

    pos = np.array([0., 0.]) # actual x,y position of pen
    down = False
    servo_x = Servo('x')
    servo_y = Servo('y')
    servo_z = Servo('pen')

    new_pos = None # target x,y position of pen
    v = 0 # speed vector to get in n steps to the new_pos, depending on self.SPEED
    n = 0

    pl = pl.Plot()

    # sets a new target position
    # caculates movement variables
    # but does not move pen yet
    def preset(self, new_pos):
        self.new_pos = new_pos
        x = self.new_pos[0]
        y = self.new_pos[1]
        self.calc_number_of_steps()
    
    def get_distance(self):
        return la.norm(self.new_pos - self.pos)

    # calculate the number of steps needed to move to new_pos with given SPEED
    def calc_number_of_steps(self):
        d = self.get_distance()
        n = int((divmod(d, cm.SPEED * cm.PERIOD / 1000)[0] + 1))
        self.number_of_steps = n
        return n

    def get_step(self):
        step = np.array([0,0])
        delta = (self.new_pos - self.pos)
        step = delta / self.number_of_steps
        return step
    
    # move the servos
    def move_servos(self, pos):
        self.servo_x.move(pos[0])
        self.servo_y.move(pos[1])

        if self.debug: # only for testing purposes
            print('move_servos', pos[0], pos[1])
            self.pl.point(pos[0], pos[1])

    # move pen up or down
    def move_pen_down(self, down):
        if down:
            self.servo_z.set(0)
        else:
            self.servo_z.set(1000)
        if self.debug: print('up/down')
        sleep(cm.UP_DOWN_DURATION / 1000)

    # move the pen to the target
    def move(self):
        number_of_steps = self.calc_number_of_steps()
        delta = self.get_step()
        for step in range(0, number_of_steps):
            # move servos
            if step < number_of_steps - 1:
                self.pos = self.pos + delta
                self.move_servos(self.pos)
            else:
                # move to final position
                self.pos = self.new_pos
                self.move_servos(self.new_pos)

            # wait period
            sleep(cm.PERIOD / 1000)

    # move pen according to this gcode command (x,y must be in 0..1000)
    def cmd(self, cmd: gp):
        if self.down != cmd.pen_down:
            self.move_pen_down(cmd.pen_down)
            self.down = cmd.pen_down
        self.preset(np.array([cmd.x, cmd.y]))
        self.move()