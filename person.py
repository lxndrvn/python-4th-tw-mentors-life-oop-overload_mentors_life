import random


class Person:
    Gender = ['male', 'female', 'not sure']

    def __init__(self, first_name, last_name, year_of_birth, gender, energy_level, happiness_level):
        if gender not in self.Gender:
            raise ValueError('%s is not a valid gender.' % gender)

        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = int(year_of_birth)
        self.gender = gender
        self.energy_level = int(energy_level)
        self.happiness_level = int(happiness_level)

    def drink_coffee(self, delta):
        self.energy_level += int(delta)
        
        return self.energy_level

    def smoke(self, delta):
        self.happiness_level += int(delta)
        self.energy_level += int(delta)
        
        return self.happiness_level
        
        return self.energy_level
