class Circle():
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2

#driver code
circle = Circle(10)
print(circle.area())

