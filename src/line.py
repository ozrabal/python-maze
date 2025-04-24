from .point import Point

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        
    def draw(self, canvas, fill_color):
        """
        Draw this line on the canvas with the specified fill color
        
        Args:
            canvas: The canvas to draw on
            fill_color: String color name ("black", "red", etc.)
        """
        # Draw the line on the canvas
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )