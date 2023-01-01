# a position is a valid position if self.valid is True and self.end is False
# only then, x, y and pen_down shall be valid
class Gcode_pos:

    def __init__(self, x = None, y = None, pen_down = False, end = False) -> None:
        self.x = x
        self.y = y
        self.pen_down = pen_down
        self.end = end
        self.valid = True
    
    def __eq__(self, pos) -> bool:
        return (self.x == pos.x and self.y == pos.y and self.pen_down == pos.pen_down and self.end == pos.end and self.valid == pos.valid)