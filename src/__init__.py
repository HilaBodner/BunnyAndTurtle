import asyncio

from Animals.Bunny import Bunny
from Animals.Turtle import Turtle
from Animals.CompetingAnimal import CompetingAnimal
from Road import Road

havi = CompetingAnimal("Havi the bunny", 0, 3, 'B')
tirza = CompetingAnimal("Tirza the turtle", 0, 1, 'T')
all_animals = [havi, tirza]
race_road = Road(20)
race_length = race_road.length_in_steps


def race_is_over(animals: list):
    for animal in all_animals:
        if animal.has_won(race_length):
            return True
    return False


def print_result(animals: list):
    for animal in animals:
        if animal.has_won(race_length):
            print(animal.name + ' won!')


async def compete(animals: list):
    while not race_is_over(animals):
        await asyncio.sleep(1)
        print("RACE STATUS")
        print('----------------------------------------------------')
        for animal in animals:
            print(" ".join(animal.run()))
        print('----------------------------------------------------')

    print_result(animals)


asyncio.run(compete(all_animals))
