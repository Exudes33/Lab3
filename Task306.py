class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    
    def area(self):
        return self.length * self.width

a = list(map(int, input().split()))
L = a[0]
W = a[1]


rect = Rectangle(L, W)
print(rect.area())
