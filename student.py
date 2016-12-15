import csv
from person import Person
from project import Project



class Student(Person):
    def __init__(self, first_name, last_name, year_of_birth, gender, energy_level, happiness_level, knowledge_level):
        super().__init__(first_name, last_name, year_of_birth, gender, energy_level, happiness_level)
        self.knowledge_level = knowledge_level

    @staticmethod
    def create_by_csv(csv_file):
        with open(csv_file, "r") as data:
            students = csv.reader(data)
            list_of_students = [Student(row[0], row[1], row[2], row[3], row[4]) for row in students]
        return list_of_students
    
    def work_on_project(self, project):
        project.code_complete = True
        self.knowledge += 10
        print("Student {} has worked on project {}").format(self.name, project.name)
