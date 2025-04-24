from window import Window
from point import Point
from line import Line
from cell import Cell # Import Cell

def main():
    win = Window(800, 600)
 
    # Create a few points
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(300, 100)
    p4 = Point(100, 300)
    p5 = Point(400, 400)
    
    # Create and draw lines using the points
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p1)
    line4 = Line(p2, p5)
    line5 = Line(p4, p5)
    
    # Draw lines with different colors
    win.draw_line(line1, "yellow")
    win.draw_line(line2, "blue")
    win.draw_line(line3, "green")
    win.draw_line(line4, "black")
    win.draw_line(line5, "red")

    # Create cells
    cell1 = Cell(win)
    cell1.draw(50, 50, 100, 100) # Draw a standard cell

    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.draw(150, 50, 200, 100) # Draw cell with no left wall

    cell3 = Cell(win)
    cell3.has_top_wall = False
    cell3.has_right_wall = False
    cell3.draw(50, 150, 100, 200) # Draw cell with no top or right wall

    cell4 = Cell(win)
    cell4.has_bottom_wall = False
    cell4.draw(150, 150, 200, 200) # Draw cell with no bottom wall

    cell5 = Cell(win)
    cell5.has_left_wall = False
    cell5.has_right_wall = False
    cell5.has_top_wall = False
    cell5.has_bottom_wall = False
    cell5.draw(250, 100, 300, 150) # Draw cell with no walls

    win.wait_for_close()

if __name__ == "__main__":
    main()