import Person from person
import Project from project


class Student(Person):
    def __init__(self, first_name, last_name, year_of_birth, gender, work_on_project = False):
        Person.__init__(self, first_name, last_name, year_of_birth, gender)
        Project.__init__(self, work_on_project)

    @staticmethod
    def create_by_csv(csv_file):
        with open(csv_file, "r") as data:
            students = csv.reader(data)
            list_of_students = [Student(row[0], row[1], row[2], row[3], row[4]) for row in students]
        return list_of_students
    
    def work_on_project(project):
        return project.code_complete = True
