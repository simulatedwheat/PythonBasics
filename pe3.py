# Programming Excercises Chapter 3

import math



def volume():
    print("This function takes the radius as input to calculate the volume and surface area of a sphere.")
    radius = float(input("Enter the radius: "))
    volume = 4/3*math.pi*radius**3
    surfaceArea = 4*math.pi*radius**2
    print("Volume:", volume, "\nSurface Area:", surfaceArea)

####
volume()