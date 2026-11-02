###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
cuboid_volue = a * b * c 
cuboid_surfacearea = (2*a*b) + (2*a*c) + (2*b*c)

print(cuboid_volue)
print(cuboid_surfacearea)