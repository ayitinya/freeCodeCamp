import math


class Rectangle:
    width = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return type(self).__name__ + "(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        perim = self.width * 2 + self.height * 2
        return perim

    def get_diagonal(self):
        diag = math.sqrt(pow(self.width, 2) + pow(self.height, 2))
        return diag

    def set_width(self, w):
        self.width = w
        return True

    def set_height(self, h):
        self.height = h
        return True

    #  * `get_picture`: Returns a string that represents the shape using lines of "\*".
    #  The number of lines should be equal to the height and the number of "\*" in each line should be equal to the width.
    #  There should be a new line (`\n`) at the end of each line.
    #  If the width or height is larger than 50, this should return the string: "Too big for picture.
    def get_picture(self):

        if (self.width > 50 or self.height > 50):
            return "Too big for picture."
        else:
            pic = ''
            char = "*"
            for iter in range(self.height):
                line = (char * self.width)
                pic = pic + line + "\n"
            return pic

    # * `get_amount_inside`: Takes another shape (square or rectangle) as an argument
    #  Returns the number of times the passed in shape could fit inside the shape (with no rotations)
    #  For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4
    def get_amount_inside(self, shape):
        wCount = math.floor(self.width / shape.width)
        hCount = math.floor(self.height / shape.height)
        return wCount * hCount


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return type(self).__name__ + "(side=" + str(self.width) + ")"

    def set_side(self, side):
        self.width = side
        self.height = side
        return True
