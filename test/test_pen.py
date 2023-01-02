import unittest
from pen import *

class Test(unittest.TestCase):

    def test_init(self):
        pen = Pen()
        self.assertTrue(np.array_equal(pen.pos, np.array([0,0])))
        self.assertFalse(pen.down)

    def test_preset(self):
        pen = Pen()
        pen.preset(np.array([50,50]))
        self.assertTrue(True)

    def test_distance(self):
        pen = Pen()
        pen.pos = np.array([0,0])
        pen.preset(np.array([1000,0]))
        self.assertEqual(pen.get_distance(), 1000)
        pen.preset(np.array([0,1000]))
        self.assertEqual(pen.get_distance(), 1000)
        pen.preset(np.array([3,4]))
        self.assertEqual(pen.get_distance(), 5)

    def test_step(self):
        pen = Pen()
        pen.preset(np.array([0,500]))
        print(f'get_step: {pen.get_step()} ')
        self.assertTrue(np.array_equal(pen.get_step(), np.array([0, 500/51])))

    def test_number_of_steps(self):
        pen = Pen()
        pen.preset(np.array([0,500]))
        self.assertEqual(pen.number_of_steps, 51)

        pen.preset(np.array([0,100]))
        self.assertEqual(pen.number_of_steps, 11)

        pen.preset(np.array([1,0]))
        self.assertEqual(pen.number_of_steps, 1)
    
    def test_move(self):
        pen = Pen()
        pen.preset(np.array([100,200]))
        pen.move()

        pen2 = Pen()
        pen.preset(np.array([1,1]))
        pen.move()

    def test_cmd(self):
        pen = Pen()
        self.assertEqual(pen.pos[0], 0.0)
        self.assertEqual(pen.pos[1], 0.0)
        
        pen.cmd(gp(True, 55, 66))
        self.assertEqual(pen.pos[0], 55.0)
        self.assertEqual(pen.pos[1], 66.0)
