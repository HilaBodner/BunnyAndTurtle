import asyncio

from Animals.Bunny import Bunny
from Animals.Turtle import Turtle
from Animals.CompetingAnimal import CompetingAnimal
from Road import Road

havi = CompetingAnimal("Havi the bunny", 0, 3, 'B')
tirza = CompetingAnimal("Tirza the turtle", 0, 1, 'T')

all_animals = [havi, tirza]

race_road = Road(20)


async def compete(all_animals):
    while not havi.has_won(race_road.length_in_steps) and not tirza.has_won(race_road.length_in_steps):
        await asyncio.sleep(1)
        print("RACE STATUS")
        print('----------------------------------------------------')
        for animal in all_animals:
            print(" ".join(animal.run()))
        print('----------------------------------------------------')

    for animal in all_animals:
        if animal.has_won(race_road.length_in_steps):
            print(animal.name + ' won!')


asyncio.run(compete(all_animals))
