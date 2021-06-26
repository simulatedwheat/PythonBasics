# Programming Excercises Chapter 3

import math



def volume():
    print("This function takes the radius as input to calculate the volume and surface area of a sphere.")
    radius = float(input("Enter the radius: "))
    volume = 4/3*math.pi*radius**3
    surfaceArea = 4*math.pi*radius**2
    print("Volume:", volume, "\nSurface Area:", surfaceArea)

def squareInch():
    print("This function calculates the prize per square inch of circular objects.")
    diameter = float(input("Enter the diameter in inches: "))
    cost = float(input("Enter the cost: "))
    radius = diameter / 2
    area = math.pi*radius**2
    costPerSqInch = area / cost
    print("The cost per square inch is:", costPerSqInch)

def lightningDist():
    print("This function calculates the distance to a lightning strike based on how long it takes to hear the sound.")
    # Speed of sound 343m/s
    # 1km = 1000m
    time = int(input("Enter the time it took from the flash to the thunder in seconds: "))
    m = time * 343
    if m > 999:
        km = m / 1000
        print("The lightning was",km, "km away")
    else:
        print("The lightning was",m, "meters away")

def slope():
    print("This function calculates the slope of a line through two non vertical points.")
    x1 = float(input("Enter the X value of the first point: "))
    y1 = float(input("Enter the Y value of the first point: "))
    x2 = float(input("Enter the X value of the second point: "))
    y2 = float(input("Enter the Y value of the second point: "))
    slope = (y2-y1)/(x2-x1)
    print(slope)

#def easter():
 #   print("This function calculates when easter is")
  #  year = eval(input("Enter the year: "))
   # C = year / 100
    #x = (8+(C/4) - C + ((8*C + 13)/25) + 11(year%19))%30
    #print(x)

####
#volume()
#squareInch()
#lightningDist()
#slope()
#easter()