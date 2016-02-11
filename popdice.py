#!/usr/bin/env python3
from random import choice
    

def pop_dice(face):
    faces = [i for i in range(1, face+1)]
    while faces != []:
        input("Dice! (enter) >>")
        number = choice(faces)
        print(number)
        faces.remove(number)

if __name__ == '__main__':
    people = input('How many people? >>>')
    pop_dice(int(people))

