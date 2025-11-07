class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter


pythagorean_triple = Triangle(3,4,5)
result = pythagorean_triple.perimeter()
print(f'The perimeter is {result} units.')

#This program was written on 11/6/25 by Logan Gibson
#Its name is "Triangle Perimeter Calculator"