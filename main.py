from graphics import Window, Line, Point
from cell import Cell


def main():
    win = Window(800, 600)

    c = Cell(win)
    c.draw(25, 25, 50, 50)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(100, 100, 125, 135)

    c = Cell(win)
    c.has_bottom_wall = False
    c.has_right_wall = False
    c.draw(125, 125, 150, 150)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(200, 200, 225, 225)

    win.wait_for_close()


main()
