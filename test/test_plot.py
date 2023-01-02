import unittest
from plot import *
from gcode import *

class TestPlot(unittest.TestCase):

    @unittest.skip("plot is only for debugging reasons")
    def test_show(self):
        pl = Plot()

        pl.point(1,1)
        pl.point(2,2)
        pl.point(8,3)

        pl.show()

    @unittest.skip("plot is only for debugging reasons")
    def test_long(self):
        pl = Plot()

        gc = Gcode()
        gc.parse('./data/long.nc')

        for cmd in gc.cmds:
            pl.point(cmd.x, cmd.y)
        
        pl.show()

