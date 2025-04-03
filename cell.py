from graphics import Line, Point

class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        left_wall = Line(Point(x1, y1), Point(x1,y2))
        bottom_wall = Line(Point(x1, y2), Point(x2, y2))
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        right_wall = Line(Point(x2, y1), Point(x2, y2))
        if self.has_left_wall:
            self._win.draw_line(left_wall)
        else:
            self._win.draw_line(left_wall, "white")
        if self.has_right_wall:
            self._win.draw_line(right_wall)
        else:
            self._win.draw_line(right_wall, "white")
        if self.has_top_wall:
            self._win.draw_line(top_wall)
        else:
            self._win.draw_line(top_wall, "white")
        if self.has_bottom_wall:
            self._win.draw_line(bottom_wall)
        else:
            self._win.draw_line(bottom_wall, "white")

    def draw_move(self, to_cell, undo=False):
        center_a_x = (self._x1 + self._x2) / 2
        center_a_y = (self._y1 + self._y2) / 2
        center_b_x = (to_cell._x1 + to_cell._x2) / 2
        center_b_y = (to_cell._y1 + to_cell._y2) / 2
        color_fill = "red"
        if undo:
            color_fill = "gray"
        
        line = Line(Point(center_a_x, center_a_y), Point(center_b_x, center_b_y))
        self._win.draw_line(line, color_fill)
