from window import Window
from point import Point
from line import Line

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

    win.wait_for_close()

if __name__ == "__main__":
    main()