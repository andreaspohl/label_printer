from gcode import *
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
        self.assertEqual(gc.decode(''), None)
        self.assertRaisesRegex(Exception, 'Unknown gcode: G2', gc.decode, 'G2')   

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

    def test_normalize(self):
        gc = Gcode()
        gc.parse_test2()
        gc.create_cmd_list()
        gc.normalize()
        for i in range(len(gc.cmds)):
            if i == 0:
                self.assertEqual(gc.cmds[0], gp(True, 0.0, 0.0))
            elif i == 1:
                self.assertEqual(gc.cmds[1], gp(True, 1000.0, 1000.0))
            elif i == 2:
                self.assertEqual(gc.cmds[2], gp(True, 2000.0, 0.0))
    
    def test_print(self):
        gc = Gcode()
        gc.parse_test2()
        gc.create_cmd_list()
        gc.normalize()

        print('Lines:')
        for line in gc.lines:
            print(line)
        print()

        print('Commands:')
        for cmd in gc.cmds:
            print(cmd.pen_down, cmd.x, cmd.y)
