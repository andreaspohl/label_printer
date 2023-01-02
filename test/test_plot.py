import unittest
from plot import *

class TestServo(unittest.TestCase):

    def test_show(self):
        pl = Plot()

        pl.point(1,1)
        pl.point(2,2)
        pl.point(8,3)

        pl.show()
