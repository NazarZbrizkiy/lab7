import math

class Figure:
    def dimention(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def square(self):
        raise NotImplementedError

    def squareSurface(self):
        raise NotImplementedError

    def squareBase(self):
        raise NotImplementedError

    def height(self):
        raise NotImplementedError

    def volume(self):
        # Для 2D повертає площу, для 3D — об'єм
        if self.dimention() == 2:
            return self.square()
        elif self.dimention() == 3:
            raise NotImplementedError

# --- 2D Figures ---

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def dimention(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        return self.square()

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def dimention(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.b

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        return self.square()

class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def dimention(self):
        return 2

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        # Формула площі через сторони (Брама-Грама)
        s = (self.a + self.b + self.c + self.d) / 2
        if self.a == self.b:
            return 0
        h = (2 / abs(self.a - self.b)) * math.sqrt(
            (s - self.a) * (s - self.b) * (s - self.a - self.c) * (s - self.a - self.d)
        )
        return ((self.a + self.b) / 2) * h

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        return self.square()

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h

    def dimention(self):
        return 2

    def perimeter(self):
        return 2 * (self.a + self.b)

    def square(self):
        return self.a * self.h

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        return self.square()

class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self):
        return 2

    def perimeter(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * self.r ** 2

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        return self.square()

# --- 3D Figures ---

class Ball(Circle):
    def __init__(self, r):
        super().__init__(r)

    def dimention(self):
        return 3

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return 4 * math.pi * self.r ** 2

    def squareBase(self):
        return math.pi * self.r ** 2

    def height(self):
        return 2 * self.r

    def volume(self):
        return (4/3) * math.pi * self.r ** 3

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h

    def dimention(self):
        return 3

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        base = (math.sqrt(3) / 4) * self.a ** 2
        side = (self.a * math.sqrt((self.a/2)**2 + self.h**2))
        return 3 * side

    def squareBase(self):
        return (math.sqrt(3) / 4) * self.a ** 2

    def height(self):
        return self.h

    def volume(self):
        return (self.squareBase() * self.h) / 3

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h

    def dimention(self):
        return 3

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return self.a * math.sqrt((self.b/2)**2 + self.h**2) + self.b * math.sqrt((self.a/2)**2 + self.h**2)

    def squareBase(self):
        return self.a * self.b

    def height(self):
        return self.h

    def volume(self):
        return (self.squareBase() * self.h) / 3

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def dimention(self):
        return 3

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return 2 * (self.a*self.b + self.a*self.c + self.b*self.c)

    def squareBase(self):
        return self.a * self.b

    def height(self):
        return self.c

    def volume(self):
        return self.a * self.b * self.c

class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h

    def dimention(self):
        return 3

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        l = math.sqrt(self.r**2 + self.h**2)
        return math.pi * self.r * l

    def squareBase(self):
        return math.pi * self.r ** 2

    def height(self):
        return self.h

    def volume(self):
        return (1/3) * math.pi * self.r ** 2 * self.h

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h

    def dimention(self):
        return 3

    def perimeter(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return 2 * self.squareBase() + self.perimeter() * self.h

    def squareBase(self):
        return super().square()

    def height(self):
        return self.h

    def volume(self):
        return self.squareBase() * self.h

# --- Парсер рядка ---
def parse_figure(line):
    parts = line.strip().split()
    if not parts:
        return None
    name = parts[0]
    params = list(map(float, parts[1:]))
    if name == "Triangle" and len(params) == 3:
        return Triangle(*params)
    elif name == "Rectangle" and len(params) == 2:
        return Rectangle(*params)
    elif name == "Trapeze" and len(params) == 4:
        return Trapeze(*params)
    elif name == "Parallelogram" and len(params) == 3:
        return Parallelogram(*params)
    elif name == "Circle" and len(params) == 1:
        return Circle(*params)
    elif name == "Ball" and len(params) == 1:
        return Ball(*params)
    elif name == "TriangularPyramid" and len(params) == 2:
        return TriangularPyramid(*params)
    elif name == "QuadrangularPyramid" and len(params) == 3:
        return QuadrangularPyramid(*params)
    elif name == "RectangularParallelepiped" and len(params) == 3:
        return RectangularParallelepiped(*params)
    elif name == "Cone" and len(params) == 2:
        return Cone(*params)
    elif name == "TriangularPrism" and len(params) == 4:
        return TriangularPrism(*params)
    else:
        return None

# --- Пошук фігури з найбільшою мірою ---
import glob
import os

folder = r'c:\Users\Nosok\Downloads'
patterns = ["input*.txt", "input* (1).txt"]
files = []
for pattern in patterns:
    files.extend(glob.glob(os.path.join(folder, pattern)))

for filename in files:
    print(f"\nОбробка файлу: {os.path.basename(filename)}")
    figures = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            fig = parse_figure(line)
            if fig:
                figures.append(fig)

    max_measure = -1
    max_figure = None

    for fig in figures:
        try:
            measure = fig.volume()
        except Exception:
            continue
        if measure is not None and measure > max_measure:
            max_measure = measure
            max_figure = fig

    print("Фігура з найбільшою мірою:", type(max_figure).__name__, "Міра:", max_measure)