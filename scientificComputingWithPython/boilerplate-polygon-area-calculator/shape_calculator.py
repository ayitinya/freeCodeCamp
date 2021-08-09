import math


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"{type(self).__name__}(width={self.width}, height={self.height})"

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_area(self):
        """
        Returns area (width * height)
        :return: width * height
        """

        area = self.width * self.height
        return area

    def get_perimeter(self):
        """
        :return: perimeter (2 * width + 2 * height)
        """

        perimeter = 2 * (self.width + self.height)
        return perimeter

    def get_diagonal(self):
        """
        :return: diagonal ((width ** 2 + height ** 2) ** .5)
        """
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal

    def get_picture(self) -> str:
        """
         a string that represents the shape using lines of "*". The number of lines should be equal to the height and
         the number of "*" in each line should be equal to the width. Return 'Too big for picture' if height or width is
         greater than 50
        """
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = []
            i = 0
            while i < self.height:
                picture.append("*" * self.width)
                i += 1

        return "\n".join(picture) + "\n"

    def get_amount_inside(self, shape):
        """
        Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape
        could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8
        could fit in two squares with sides of 4
        :param shape: another square or rectangle
        :return: number of times shape fits into object
        """

        x = math.floor(self.width / shape.width)
        y = math.floor(self.height / shape.height)
        return x * y


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side
        super().__init__(self.width, self.height)

    def __str__(self):
        return f"{type(self).__name__}(side={self.height})"

    def set_side(self, side):
        self.set_height(side)
        self.set_width(side)

    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)

    def set_height(self, height):
        super().set_width(height)
        super().set_height(height)


if __name__ == "__main__":
    rect = Square(10)
