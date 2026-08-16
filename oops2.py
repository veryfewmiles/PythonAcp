class circle:
    def __init__(self,radius):
        self.radius = radius
    def circlearea(self):
        print(self.radius)
        print("The area of the circle is",3.14*self.radius*self.radius)
var1 = circle(5)
var1.circlearea()