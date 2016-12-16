from mentor import Mentor
from student import Student

class CodecoolClass:
    def __init__(self, location, year, mentors, students):
        self.location = location
        self.year = year
        self.mentors = mentors
        self.students = students    

    def check_mentors(self, full_name):
        for mentor in self.mentors:
            if mentor.first_name + ' ' + mentor.last_name == full_name:
                print("{} was found between the mentors".format(full_name))
                return mentor
            
    def check_students(self, full_name):
        def check_students(self, full_name):
            for student in self.students:
                if student.first_name + ' ' + student.last_name == full_name:
                    print("{} was found between the students".format(full_name))
                    return student

    @classmethod
    def generate_local(cls):
        location = "Budapest"
        year = 2016
        mentors = Mentor.create_by_csv()
        students = Student.create_by_csv()
        codecool_object = CodecoolClass(location, year, mentors, students)
        return codecool_object
