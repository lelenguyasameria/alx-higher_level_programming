#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

# Testing
if __name__ == '__main__':
    s1 = Square(5)
    s2 = Square(3)
    s3 = Square(5)

    print(s1 > s2)  # True
    print(s1 < s2)  # False
    print(s1 == s3)  # True
    print(s1 != s2)  # True
    print(s1 >= s3)  # True
    print(s1 <= s2)  # False

