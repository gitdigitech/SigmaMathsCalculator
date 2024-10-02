import math

def pythag(a, b=None):
    if not b:
        b = a
    a2 = a * a
    b2 = b * b
    c2 = a2 + b2
    return math.sqrt(c2)
