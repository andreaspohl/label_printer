from command import *
import unittest

class Test(unittest.TestCase):

    def test_init(self):
        pos = Command(True, 1.0, 2.0)
        self.assertEqual(pos.pen_down, True)
        self.assertEqual(pos.x, 1.0)
        self.assertEqual(pos.y, 2.0)
    
    def test_eq(self):
        pos1 = Command(True, 1.0, 2.0)
        pos2 = Command(True, 1.0, 2.0)
        pos3 = Command(False, 1.0, 2.0)
        pos4 = Command(True, 1.0, 2.1)
        self.assertEqual(pos1, pos2)
        self.assertNotEqual(pos1, pos3)
        self.assertNotEqual(pos1, pos4)
        self.assertTrue(pos1 == pos2)
        self.assertFalse(pos1 == pos3)
        self.assertTrue(pos1 != pos3)
    
    def test_sub(self):
        pos1 = Command(True, 10.0, 5.0)
        pos2 = Command(True, 9.0, 3.0)
        self.assertEqual(pos1 - pos2, Command(True, 1.0, 2.0))