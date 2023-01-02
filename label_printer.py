import gcode as gc
import pen

gc = gc.Gcode()
pen = pen.Pen()
pen.debug = True

gc.parse('./data/short.nc')

for cmd in gc.cmds:
    print('GCODE:     ', cmd.x, cmd.y)
    pen.cmd(cmd)

pen.pl.show()