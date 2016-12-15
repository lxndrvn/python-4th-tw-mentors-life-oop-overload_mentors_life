import os

from person import Person
from student import Student
import csv


class Mentor(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender, energy_level, happiness_level, nickname, soft_skill_level):
        super().__init__(first_name, last_name, year_of_birth, gender, energy_level, happiness_level)
        self.nickname = nickname
        self.soft_skill_level = int(soft_skill_level)

    def teach(self, student, delta):
        self.soft_skill_level += int(delta)
        student.knowledge_level += int(delta)
        print("Mentor {0} is teaching student {1}. Student's knowledge level is now {2}.").format(
            self.name, student.name, student.knowledge_level
        )

    def grade_project(self, name, who, code_complete):
        self.name = name
        self.who = who
        self.code_complete = code_complete

    @classmethod
    def create_by_csv(file_name="mentors.csv"):
        mentor_list = []
        path = os.path.abspath("./data/%s" % file_name)
        with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                mentor_list.append(row)
        return(mentor_list)
