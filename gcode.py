# parses a gcode file

import numpy as np
from commons import Commons as cm


class Gcode:

    lines = None # the content of the gcode file
    bookmark = 0 # line to read next
    size = 0 # number of lines

    def parse_test(self):
        lines = (
            'G01 X0.0 Y0.0',
            'G01, X100.0 Y100.0',
            'G01, X200.0 Y0.0')

    # checks if the gcodes fit into the canvas
    def trim(self):
        return 'not implemented'

    def parse(self, file):
        print('parse file')
        file = open(file, 'r')
        self.lines = file.readlines()
        file.close()

    def decode(self, cmd):
        if cmd[0] == 'X':
            return ('X', float(cmd.split('X')[1]))
        if cmd[0] == 'Y':
            return ('Y', float(cmd.split('Y')[1]))
        if cmd == cm.CODE_DOWN:
            return ('PEN', 'DOWN')
        if cmd == cm.CODE_UP:
            return ('PEN', 'UP')
        return ('ERROR', None)        

    # gets the next gcode command
    # returns it as x,y, up/down position or end of file
    def get_next(self):
        pos = None
        x = None
        y = None
        pen_down = None
        eof = None

        if self.bookmark == self.size:
            eof = True
        else:
            command = self.lines[self.bookmark]
            self.bookmark += 1
            cmds = command.split(' ')
            for cmd in cmds:
                decoded = self.decode(cmd)
                cmd_type = decoded[0]
                cmd_value = decoded[1]
                if cmd_type == 'X':
                    x = cmd_value
                elif cmd_type == 'Y':
                    y = cmd_value
                elif cmd_type == 'PEN':
                    if cmd_value == 'UP':
                        pen_down = False
                    if cmd_value == 'DOWN':
                        pen_down = True
            
            if x is not None and y is not None:
                print('tbd')



        return (type, value)


# ---------------------------------------------------------
import unittest
class Test(unittest.TestCase):

    def test_init(self):
        gcode = Gcode()
        self.assertEqual(gcode.lines, None)
    
    def test_decode(self):
        gc = Gcode()
        self.assertEqual(gc.decode('G0'), ('PEN', 'UP'))
        self.assertEqual(gc.decode('G1'), ('PEN', 'DOWN'))    
        self.assertEqual(gc.decode('X-100.0'), ('X', -100.0))    
        self.assertEqual(gc.decode('Y22'), ('Y', 22.0))    
        self.assertEqual(gc.decode('G2'), ('ERROR', None))    


if __name__ == '__main__':
    unittest.main(verbosity=2)    