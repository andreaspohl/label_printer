import gcode as gc
import pen

class Label_printer:

    def __init__(self) -> None:
        self.gc = gc.Gcode()
        self.pen = pen.Pen()
        self.pen.debug = False

    def plot_label(self, file):
        self.gc.parse(file)

        for cmd in self.gc.cmds:
            print('CMD:     ', cmd.x, cmd.y)
            self.pen.cmd(cmd)

        self.pen.pl.show()