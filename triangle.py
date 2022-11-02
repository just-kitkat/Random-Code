def tri_perimeter(a,b,c):
    perimeter = a + b + c
    return perimeter

def tri_area(b, h):
    return round(0.5*b*h, 1)

def heron_area(a, b, c):
    s = tri_perimeter(a, b, c)/2
    return (s*(s - a)*(s - b)*(s - c))**0.5

print("Perimeter of triangle is: {}".format(tri_perimeter(3,4,5)))
print("Test case - (sides 4, 6, 9). Perimeter of triangle is: {}".format(tri_perimeter(4,6,9)))
print("Test case - (sides 54, 36, 49). Perimeter of triangle is: {}".format(tri_perimeter(54,36,49)))