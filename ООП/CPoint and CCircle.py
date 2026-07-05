# Ваше определение класса CCircle
class CPoint:
    def __init__(self, x: int = 0, y: int = 0)->None:
        self.x = x
        self.y = y

    def set_coordinates(self, x: int, y: int)->None:
        self.x = x
        self.y = y

    def get_coordinates(self)->tuple:
        return (self.x, self.y)

    def reset(self) -> None:
        self.set_coordinates(0, 0)

    def calc_dist(self, point: "CPoint")->float:
        return ((point.x - self.x)**2+(point.y - self.y)**2)**0.5
class CCircle():

    def __init__(self, center: CPoint = CPoint(0, 0), radius: int = 1):
        self.center = center
        self.radius = radius

    def set_circle(self, center: CPoint, radius: int):
        self.radius = radius
        self.center = center

    def is_on_circle(self, point: CPoint) -> bool:
        return self.center.calc_dist(point) == self.radius

center = CPoint(3, -2)
circle = CCircle()
circle.set_circle(center, 5)
point = CPoint(0, 2)
print(circle.is_on_circle(point))


