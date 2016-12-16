from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from project import Project
from lunchbreak import Lunchbreak
from yoga import Yoga

codecool_bp = CodecoolClass.generate_local()
oop_project = Project('OOP')


print('A new day just started at Codecool. Our mentors are:')

for mentor in codecool_bp.mentors:
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

input()

codecool_bp.check_mentors("Immánuel Fodor")

input()

print('First everyone has a coffee and a cigarette.')
for mentor in codecool_bp.mentors:
    print(mentor.nickname)
    mentor.smoke(10)
for student in codecool_bp.students:
    print(student.first_name)
    student.smoke(10)

input()

codecool_bp.mentors[0].teach(codecool_bp.students[0], 10)

student = codecool_bp.students[2]
mentor = codecool_bp.mentors[2]
lunch = Lunchbreak(student.happiness_level, student.energy_level, student.knowledge_level, mentor.soft_skill_level)
lunch.story_line_changer()

input()

student = codecool_bp.students[2]
mentor = codecool_bp.mentors[2]
lunch = Lunchbreak(student.happiness_level, student.energy_level, student.knowledge_level, mentor.soft_skill_level)
lunch.story_line_changer()

input()

codecool_bp.students[1].work_on_project(oop_project)
codecool_bp.mentors[1].grade_project(oop_project, 5, 10)

input()
yoga = Yoga(student.happiness_level, student.energy_level, student.knowledge_level, mentor.soft_skill_level)
yoga.story_line_changer()

