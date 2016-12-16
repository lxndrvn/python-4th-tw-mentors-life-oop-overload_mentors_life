import os
import csv

from person import Person
from student import Student

class Mentor(Person):
    def __init__(self, first_name, last_name, year_of_birth, gender, energy_level, happiness_level, nickname, soft_skill_level):
        super().__init__(first_name, last_name, year_of_birth, gender, energy_level, happiness_level)
        self.nickname = nickname
        self.soft_skill_level = int(soft_skill_level)

    def teach(self, student, delta, mentor):
        self.soft_skill_level += int(delta)
        student.knowledge_level += int(delta)
        mentor.soft_skill_level += int(delta)
        print("Mentor {0} is teaching student {1}. Student's knowledge level is now {2}. And the mentor's soft skill level is now {3} ").format(
            self.name, student.name, student.knowledge_level, mentor.soft_skill_level)

    def grade_project(self, project, grade, delta):
        project.grade = grade
        self.soft_skill_level += int(delta)
        print("Mentor {0} gave a {1} for project {2}. Mentor's soft skill level is now {3}.").format(
        self.nickname, grade, project.name, self.soft_skill_level)

    @classmethod
    def create_by_csv(cls, file_name="mentors.csv"):
        mentor_list = []
        path = os.path.abspath("./data/%s" % file_name)
        with open(path, newline='') as csv_file:
            reader = csv.reader(csv_file)
        for row in reader:
            new_mentor = Mentor(*row)
            mentor_list.append(new_mentor)
        return mentor_list
    
