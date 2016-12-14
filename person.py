import random


class Person:
    Gender = ['male', 'female', 'not sure']

    def __init__(self, first_name=None, last_name=None,
                 year_of_birth=None, gender=None, energy_level, happiness_level, nicotine_level):
        if gender not in self.Gender:
            raise ValueError('%s is not a valid gender.' % gender)

        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = int(year_of_birth)
        self.gender = gender
        self.energy_level = int(energy_level)
        self.happiness_level = int(happiness_level)

    def energy_level_changer(self, delta):
        self.energy_level += int(delta)
        return self.energy_level

    def happiness_level_changer(self, delta):
        self.happiness_level += int(delta)
        return self.happiness_level

    def nicotine_level_changer(self, delta):
        self.nicotine_level += int(delta)
        return self.nicotine_level

    def nicotine_level_charger(self):
        if self.energy_level < 100:
            self.energy_level += 25
        if self.happiness_level < 100:
            self.energy_level += 20
        if self.nicotine_level < 100:
            self.nicotine_level += 50
