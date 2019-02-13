# ---------------------------------------------------------------------------- #
#                                    Vectors
# ---------------------------------------------------------------------------- #
'''
Task
You are given four points A, B, C and D in a 3-dimensional Cartesian coordinate
system. You are required to print the angle between the plane made by the points
A, B, C and B, C, D in degrees(not radians). Let the angle be PHI.

Cos(PHI) = (X.Y)/|X||Y| where X = ABxBC and Y = BCxCD.

X.Y means the dot product of X and Y
ABxBC  means the cross product of vectors
AB = B-A
--------------------------------------------------------------------------------
Input Format
One line of input containing the space separated floating number values of the
X,Y and Z coordinates of a point.
Sample Input
0 4 5
1 7 6
0 5 9
1 7 2
--------------------------------------------------------------------------------
Output Format
Output the angle correct up to two decimal places.
Sample Output
8.19
--------------------------------------------------------------------------------
Formula
# AB = B-A
# a.sub(b)
# B - A  = (Bx - Ax; By - Ay; Bz - Az)

# cross product vectors
# cross ABxBC = a.sub(b) x b.sub(c) = AxB
# (Ay*Bz - Az*By; Az*Bx - Ax*Bz; Ax*By - Ay*Bx)

#dot product vectors
# a.b
# Ax*Bx + Ay*By + Az*Bz

'''
import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        return Points(other.x - self.x, \
                      other.y - self.y, \
                      other.z - self.z)

    def dot(self, other):
        return (self.x*other.x) + (self.y*other.y) + (self.z*other.z)

    def cross(self, other):
        return Points(self.y*other.z - self.z*other.y, \
                     self.z*other.x - self.x*other.z, \
                     self.x*other.y - self.y*other.x)


    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))

# ---------------------------------------------------------------------------- #
#                                   13/02/2019
# ---------------------------------------------------------------------------- #
