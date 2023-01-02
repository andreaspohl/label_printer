import gcode as gc
import pen

gc = gc.Gcode()
pen = pen.Pen()

gc.parse('./data/short.nc')

for cmd in gc.cmds:
    print(cmd.x, cmd.y)
    pen.cmd(cmd)

pen.pl.show()