from person import Person


class Student(Person):
    def __init__(self, first_name, last_name, year_of_birth, gender, knowledge_level = 0):
        super.__init__(self, first_name, last_name, year_of_birth, gender)
        self.knowledge_level = knowledge_level

    @staticmethod
    def create_by_csv(csv_file):
        with open(csv_file, "r") as data:
            students = csv.reader(data)
            list_of_students = [Student(row[0], row[1], row[2], row[3], row[4]) for row in students]
        return list_of_students
    
    def knowledge_level_charger(amount):
        return self.knowledge_level += amount
