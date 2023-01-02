# parses a gcode file

import numpy as np
from commons import Commons as cm
from gcode_pos import Gcode_pos as gp


class Gcode:

    lines = None # the content of the gcode file
    bookmark = 0 # line to read next
    size = 0 # number of lines
    cmds = list(()) # the (eventually normalized) list of machine commands aka positions

    def parse_test(self):
        self.lines = [
            'G1 X0.00 Y0.00',
            'G1 X100.00 Y100.00',
            '',
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

    def create_cmd_list(self):
        for line in self.lines:
            pos = self.decode(line)
            if pos is not None:
                self.cmds.append(pos)

    # calculates factor to fit height into 0..1000
    def normalize(self):
        print('tbd')

    # decodes a line in the nc file and returns a position (machine command)
    # G1 X4.64 Y6.04 --> pen is down, x=4.64, y=6.04
    # if the line cannot be decoded, None is returned
    def decode(self, cmd: str):
        pos = None
        if (len(cmd) > 0 and not cmd.isspace()):
            pos = gp()
            sub_cmds = cmd.split(' ')
            for sub_cmd in sub_cmds:
                if sub_cmd[0] == 'X':
                    pos.x = float(sub_cmd.split('X')[1])
                elif sub_cmd[0] == 'Y':
                    pos.y = float(sub_cmd.split('Y')[1])
                elif sub_cmd == cm.CODE_DOWN:
                    pos.pen_down = True
                elif sub_cmd == cm.CODE_UP:
                    pos.pen_down = False
                else:
                    # invalid/unknown gcode
                    pos = None
                    break
        return pos

    # resets to first line in gcode
    def reset(self):
        self.bookmark = 0
    
    # gets the next gcode command
    # returns the next machine position
    # deprecated
    def get_next(self):
        pos = gp()

        if self.bookmark == self.size:
            pos = None
        else:
            command = self.lines[self.bookmark]
            self.bookmark += 1
            sub_cmds = command.split(' ')
            for sub_cmd in sub_cmds:
                decoded = self.decode(sub_cmd)
            
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
        self.assertEqual(gc.decode('G0 X7.64 Y3.10'), gp(False, 7.64, 3.10))
        self.assertEqual(gc.decode('G1 X17.95 Y-0.01'), gp(True, 17.95, -0.01))    
        self.assertEqual(gc.decode('G2'), None)   
        self.assertEqual(gc.decode(''), None)

    def test_cmds(self):
        gc = Gcode()
        gc.parse_test()
        self.assertEqual(len(gc.lines), 4)
        gc.create_cmd_list()
        self.assertEqual(len(gc.cmds), 3)
        for i in range(len(gc.cmds)):
            if i == 0:
                self.assertEqual(gc.cmds[0], gp(True, 0.0, 0.0))
            elif i == 1:
                self.assertEqual(gc.cmds[1], gp(True, 100.0, 100.0))
            elif i == 2:
                self.assertEqual(gc.cmds[2], gp(True, 200.0, 0.0))

if __name__ == '__main__':
    unittest.main(verbosity=2)    