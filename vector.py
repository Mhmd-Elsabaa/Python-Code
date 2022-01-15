from math import sqrt, acos, pi
from decimal import Decimal, getcontext
getcontext().prec = 30

class vector(object):
    msg = "can not normalize zero vector"
    def __init__(self,coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(Decimal(x) for x in coordinates)
            self.dimension = len(coordinates)
        except ValueError:
            print("value error")
        except TypeError:
            print("TypeError")
    def __str__(self):
        return 'vector : {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates
    def scal(self,c):
        return vector([i*Decimal(c) for i in self.coordinates])
    def magnitude(self):
        coordinatesSquar = [x ** 2 for x in self.coordinates]
        return sqrt(sum(coordinatesSquar))
    def normalize(self):
        try:
            magnitude = self.magnitude()
            return self.scal(1.0/magnitude)
        except ZeroDivisionError:
            raise ZeroDivisionError(self.msg)
    def dot(self,v):
        return sum([x*y for x, y in zip(self.coordinates, v.coordinates)])
    def angle(self,v,with_degree= False):
        try:
            v1 = self.normalize()
            v2 = v.normalize()
            angle_in_radians = acos(v1.dot(v2))
            if with_degree:
                x = 180. /pi
                return angle_in_radians* x
            else:
                return angle_in_radians
        except Exception as e:
            if str(e) == self.msg:
                raise Exception('can not compute zero vector')
            else:
                raise e
    def minus(self,v):
        new_v = [x-y for x, y in zip(self.coordinates, v.coordinates)]
        return new_v
    def plus(self,v):
        new_v = [x+y for x, y in zip(self.coordinates, v.coordinates)]
        return new_v
    def is_orthogonal(self,v,tolerance = 1e-10):
        return abs(self.dot(v)) < tolerance
    def is_parallel(self,v):
        return (self.is_zero()
                or v.is_zero()
                or self.angle(v) == 0
                or self.angle(v) == pi
                )
    def is_zero(self,tolerance = 1e-10):
        return self.magnitude() < tolerance


m = vector([0, 0, 0])
n = vector([1, 3, 2])
c = m.is_orthogonal(n)

print(c)