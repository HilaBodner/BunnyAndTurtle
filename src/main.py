import asyncio
import json

from Animals.CompetingAnimal import CompetingAnimal
from Road import Road

with open("config.json") as json_data_file:
    data = json.load(json_data_file)

havi = CompetingAnimal("Havi", data["bunny"]["start_point"], data["bunny"]["step_per_sec"], data["bunny"]["step_sign"])
tirza = CompetingAnimal("Tirza", data["turtle"]["start_point"], data["turtle"]["step_per_sec"],
                        data["turtle"]["step_sign"])
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
