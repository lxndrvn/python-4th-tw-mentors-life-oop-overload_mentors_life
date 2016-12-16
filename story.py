from codecool_class import CodecoolClass
from mentor import Mentor
from project import Project
from student import Student

code_cool_bp = CodecoolClass.generate_local()
oop_project = Project('OOP')
mentors = Mentor.create_by_csv()
students = Student.create_by_csv()

print('A new day just started at Codecool. Our mentors are:')
for mentor in mentors:
    print('{0} {1} ({2}): born in {3}. Energy level is {4}, happiness level is {5} and soft skill level is {6}.\n'.format(
            mentor.first_name,
            mentor.last_name,
            mentor.nickname,
            mentor.year_of_birth,
            mentor.energy_level,
            mentor.happiness_level,
            mentor.soft_skill_level
        )
    )

# same for students

input()

print('First everyone has a coffee and a cigarette.')
print('First everyone has a coffee and a cigarette.')
for mentor in mentors:
    print(mentor.nickname)
    mentor.smoke(10)
for student in students:
    print(student.first_name)
student.smoke(10)