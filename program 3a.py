class Shape:
    width = 0
    def __init__(self, width):
        self.width = width

class Square(Shape):
    name = "Square"
    def get_area(self):
        return self.width ** 2
    
class Triangle(Shape):
    name = "Triangle"
    height = 0 
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return 0.5 * self.width * self.height
    
SquareX = Square(5)
TriangleY = Triangle(5, 3)

print("Persegi (sisi = 5)")
print(f"Luas Persegi = {SquareX.get_area()}")
print("\nSegitiga (sisi = 5, tinggi = 3)")
print(f"Luas Segitiga = {TriangleY.get_area()}")