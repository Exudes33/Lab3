class Shape:
    def area(self):
        return 0 

class Square(Shape):
    def __init__(self, length):
        self.length = length 

    
    def area(self):
        return self.length ** 2

n = int(input())

my_square = Square(n)

print(my_square.area())
