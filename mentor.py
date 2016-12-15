from person import Person
from student import Student
import csv


class Mentor(Person):

    def __init__(self, nickname, soft_skill_level):
        super().__init__(*args)
        self.fullname = fullname
        self.soft_skill_level = int(soft_skill)

    def teach():
        self.soft_skill_level += int(delta)
        student.knowledge_level += int(delta)
        return student

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
