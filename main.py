print("Welcome to Sigma Maths Calculator! version 0.1")
from imports import *

print("Square:", measurement.area(3), "m2")
print("Rect:", measurement.area(3, 4), "m2")
perimeter, area = measurement.circle(10)
print("Circle:", perimeter, "m, ", area, "m2")
print("Diagonal length of square: ", trigonometry.pythag(1), "m2")
print("Diagonal length of rect: ", trigonometry.pythag(2, 3), "m2")
