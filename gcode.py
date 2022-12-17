# parses a gcode file

import numpy as np
from commons import Commons as cm


class Gcode:

    lines = None # the content of the gcode file
    bookmark = 0 # line to read next
    size = 0 # number of lines

    def parse_test(self):
        self.lines = [
            'G01 X0.0 Y0.0',
            'G01 X100.0 Y100.0',
            'G01 X200.0 Y0.0']
        self.size = len(self.lines)

    # checks if the gcodes fit into the canvas
    def trim(self):
        return 'not implemented'

    def parse(self, file):
        print('parse file')
        file = open(file, 'r')
        self.lines = file.readlines()
        file.close()
        self.size = len(self.lines)

    def decode(self, cmd):
        if cmd[0] == 'X':
            return ('x', float(cmd.split('X')[1]))
        if cmd[0] == 'Y':
            return ('y', float(cmd.split('Y')[1]))
        if cmd == cm.CODE_DOWN:
            return ('pen_down', True)
        if cmd == cm.CODE_UP:
            return ('pen_down', False)
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
                if cmd_type == 'x':
                    x = cmd_value
                elif cmd_type == 'y':
                    y = cmd_value
                elif cmd_type == 'pen_down':
                    pen_down = cmd_value
            
        return (pen_down, x, y)


# ---------------------------------------------------------
import unittest
class Test(unittest.TestCase):

    def test_init(self):
        gcode = Gcode()
        self.assertEqual(gcode.lines, None)
    
    def test_decode(self):
        gc = Gcode()
        self.assertEqual(gc.decode('G00'), ('pen_down', False))
        self.assertEqual(gc.decode('G01'), ('pen_down', True))    
        self.assertEqual(gc.decode('X-100.0'), ('x', -100.0))    
        self.assertEqual(gc.decode('Y22'), ('y', 22.0))    
        self.assertEqual(gc.decode('G2'), ('ERROR', None))   

    def test_get_next(self):
        gc = Gcode()
        gc.parse_test()
        self.assertEqual(gc.get_next(), (True, 0.0, 0.0))
        self.assertEqual(gc.get_next(), (True, 100.0, 100.0))
        self.assertEqual(gc.get_next(), (True, 200.0, 0.0))



if __name__ == '__main__':
    unittest.main(verbosity=2)    