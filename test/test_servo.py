import unittest
from servo import *

class TestServo(unittest.TestCase):

    def test_set(self):
        s = Servo()
        s.set(500)
        self.assertEqual(s.pos,  500)
    
    def test_limits(self):
        s = Servo()
        s.set(s.max + 1)
        self.assertEqual(s.pos, s.max)
        s.inc()
        self.assertEqual(s.pos, s.max)
        s.set(s.min - 10)
        self.assertEqual(s.pos, s.min)
        s.decr(3)
        self.assertEqual(s.pos, s.min)

    def test_inc(self):
        s = Servo()
        s.set(500)
        s.inc()
        self.assertEqual(s.pos, 501)
        s.inc(10)
        self.assertEqual(s.pos, 511)

    def test_decr(self):
        s = Servo()
        s.set(500)
        s.decr()
        self.assertEqual(s.pos, 499)
        s.decr(10)
        self.assertEqual(s.pos, 489)

    def test_pwm(self):
        s = Servo()
        s.min_pulse = 0
        s.max_pulse = 100
        s.set(500)
        self.assertEqual(s.calc_pwm(), 50)
        self.assertEqual(s.calc_pwm(700), 70)

    def test_move(self):
        s = Servo()
        s.set(500)
        s.move()
        

if __name__ == '__main__':
    unittest.main(verbosity=2)