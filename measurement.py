def area(length, width=None):
    if not width:
        return length
    else:
        return length * width

def circle(radius):
    p = 2 * 3.14 * radius
    a = 3.14 * (radius * radius)
    return (p, a) 
