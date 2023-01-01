# parses a gcode file

import numpy as np
from commons import Commons as cm
from gcode_pos import Gcode_pos as gp


class Gcode:

    lines = None # the content of the gcode file
    bookmark = 0 # line to read next
    size = 0 # number of lines
    cmds = None # the (eventually normalized) machine commands

    def parse_test(self):
        self.lines = [
            'G1 X0.00 Y0.00',
            'G1 X100.00 Y100.00',
            'G1 X200.00 Y0.00']
        self.size = len(self.lines)

    # checks if the gcodes fit into the canvas
    def trim(self):
        return 'not implemented'

    def parse(self, file):
        print('parse file')
        with open(file, 'r') as file:
            self.lines = file.readlines()
        self.size = len(self.lines)


    # calculates factor to fit height into 0..1000
    def normalize(self):
        print('tbd')

    def decode(self, sub_cmd, pos):
        if sub_cmd[0] == 'X':
            pos.x = float(sub_cmd.split('X')[1])
        elif sub_cmd[0] == 'Y':
            pos.y = float(sub_cmd.split('Y')[1])
        elif sub_cmd == cm.CODE_DOWN:
            pos.pen_down = True
        elif sub_cmd == cm.CODE_UP:
            pos.pen_down = False
        else:
            pos.valid = False
        return pos

    # resets to first line in gcode
    def reset(self):
        self.bookmark = 0
    
    # gets the next gcode command
    # returns the next machine position
    def get_next(self):
        pos = gp()

        if self.bookmark == self.size:
            pos.end = True
        else:
            command = self.lines[self.bookmark]
            self.bookmark += 1
            sub_cmds = command.split(' ')
            for sub_cmd in sub_cmds:
                decoded = self.decode(sub_cmd, pos)
            
        return (pos)


# ---------------------------------------------------------
import unittest
class Test(unittest.TestCase):

    def test_init(self):
        gcode = Gcode()
        self.assertEqual(gcode.lines, None)
    
    def test_decode(self):
        gc = Gcode()
        pos = gp()
        self.assertEqual(gc.decode('G0', pos), gp(None, None, False, False))
        self.assertEqual(gc.decode('G1', pos), gp(None, None, True, False))    
        self.assertEqual(gc.decode('X-100.0', pos), gp(-100.0, None, True, False))    
        self.assertEqual(gc.decode('Y22', pos), gp(-100.0, 22.0, True, False)) 

        invalid_pos = gp(-100.0, 22.0, True, False)
        invalid_pos.valid = False
        self.assertEqual(gc.decode('G2', pos), invalid_pos)   

    def test_get_next(self):
        gc = Gcode()
        gc.parse_test()
        self.assertEqual(gc.get_next(), gp(0.0, 0.0, True, False))
        self.assertEqual(gc.get_next(), gp(100.0, 100.0, True, False))
        self.assertEqual(gc.get_next(), gp(200.0, 0.0, True, False))
        self.assertEqual(gc.get_next(), gp(None, None, False, True))




if __name__ == '__main__':
    unittest.main(verbosity=2)    