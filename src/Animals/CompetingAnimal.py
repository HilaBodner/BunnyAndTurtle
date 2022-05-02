class CompetingAnimal:
    def __init__(self, name: str, start_point: int, step_per_sec: int, step_sign: str):
        self.name = name
        self.start_point = start_point
        self.step_per_sec = step_per_sec
        self.step_sign = step_sign
        self.steps = []
        for i in range(start_point):
            self.steps += 'X'

    def has_won(self, road_length: int):
        return road_length <= len(self.steps)

    def run(self):
        self.steps += self.step_sign * self.step_per_sec
        return self.steps
