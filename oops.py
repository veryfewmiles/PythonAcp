class Cars:
 type = "Vehicle"
def __init__(self, brand, speed):
 self.brand = brand
 self.speed = speed
car1 = Cars("BMW", 250)
car2 = Cars("Toyota", 180)
print(car1.brand, "is a", car1.type)
print(car2.brand, "is also a", car2.type)
print("{} can go {} km/h".format(car1.brand, car1.speed))
print("{} can go {} km/h".format(car2.brand, car2.speed))
print(car1.brand, "is faster then", car2.brand)