from person import Person
import csv


class Mentor(Person):

    def __init__(self, fullname, soft_skill_level):
        super().__init__(*args)
        self.fullname = fullname
        self.soft_skill_level = int(soft_skill)

    def soft_skill_level_changer(self, charger):
        self.nicotine_level += int(delta)
        return self.nicotine_level

    def create_by_csv(cls, file_name):
        mentor_list = []
        with open(file_name, "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i in reader:
                mentor_list.append(Mentor(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        return mentor_list
