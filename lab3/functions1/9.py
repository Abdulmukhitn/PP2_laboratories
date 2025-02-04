import math

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

r = float(input("Enter the radius of the sphere: "))
print(sphere_volume(r))