# a position or command in gcode
class Gcode_pos:

    def __init__(self, pen_down = False, x = None, y = None) -> None:
        self.pen_down = pen_down
        self.x = x
        self.y = y
    
    def __eq__(self, pos) -> bool:
        if pos is None:
            return False
        return (self.x == pos.x and self.y == pos.y and self.pen_down == pos.pen_down)
    
    def __ne__(self, pos) -> bool:
        return not self == pos