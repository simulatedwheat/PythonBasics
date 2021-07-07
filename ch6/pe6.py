# Programming Exercises Chapter 6
import math

###
### Number 1
###
def macdonald():
    return "Old MacDonald had a farm, Ei-igh, Ee-igh, Oh!"

def animalPart(animal):
    a = "And on that farm he had a " + animal + " Ei-igh, Ee-igh, Oh!"
    return a
def animalSound(sound):
    b = "With a " + sound + ", " + sound + " here and a " + sound + ", " + sound +" there."
    c = "\nHere a " + sound + " there a " +sound+ " everywhere a "+sound+ ", "+sound+"."
    return b + c

def song():
    animals = ["Cow", "Cat", "Dog"]
    sounds = ["moo", "meow", "Woff"]
    if len(animals) != len(sounds):
        print("List Error")
    for i in range(0,len(animals)):
        print(macdonald())
        print(animalPart(animals[i]))
        print(animalSound(sounds[i]))
        print(macdonald())
        print()

###
### Number 3
###
def sphereArea(radius):
    surfaceArea = 4*math.pi*radius**2
    return print("The surface area is:",surfaceArea)
def sphereVolume(radius):
    volume = 4/3*math.pi*radius**3
    return print("The volume is:",volume)
def sphere():
    radius = float(input("Enter the radius of a sphere: "))
    sphereArea(radius)
    sphereVolume(radius)



    
# What to run
#song()
sphere()