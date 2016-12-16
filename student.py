import csv
from person import Person
from project import Project

class Student(Person):
    def __init__(self, first_name, last_name, year_of_birth, gender, energy_level, happiness_level, knowledge_level):
        super().__init__(first_name, last_name, year_of_birth, gender, energy_level, happiness_level)
        self.knowledge_level = knowledge_level
    
    def work_on_project(self, project):
        project.code_complete = True
        self.knowledge += 10
        print("Student {} has worked on project {}").format(self.name, project.name)
    
    @staticmethod
    def create_by_csv(file_name="students.csv"):
        list_of_students = []
        path = os.path.abspath("./data/%s" % file_name)
        with open(path, newline='') as csv_file:
            students = csv.reader(csv_file)
            for row in students:
                student = Student(*row)
                list_of_students.append(student)
        return list_of_students