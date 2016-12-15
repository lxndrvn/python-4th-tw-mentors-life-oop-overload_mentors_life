from mentor import Mentor
from student import Student

class CodecoolClass:
    def __init__(self, location, year, mentors, students):
        self.location = location
        self.year = year
        self.mentors = mentors
        self.students = students
        
    @classmethod
    def generate_local(cls):
        location = "Budapest"
        year = 2016
        mentors = Mentor.create_by_csv
        students = Student.create_by_csv
        return CodecoolClass(location, year, mentors, students)

