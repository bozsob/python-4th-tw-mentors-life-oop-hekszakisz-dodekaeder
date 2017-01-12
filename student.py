import csv
from person import Person


class Student(Person):

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.year_of_birth = None
        self.gender = None
        self.knowledge_level = None
        self.energy_level = None

    @classmethod
    def create_by_csv(self, path="data/students.csv"):
        data_from_csv = []
        students = []
        with open(path, newline='') as myfile:
            for line in myfile:
                data_from_csv.append(line.strip().split(','))

        for i in range(len(data_from_csv)):
            temp_student_instance = Student()
            temp_student_instance.first_name = data_from_csv[i][0]
            temp_student_instance.last_name = data_from_csv[i][1]
            temp_student_instance.year_of_birth = data_from_csv[i][2]
            temp_student_instance.gender = data_from_csv[i][3]
            temp_student_instance.knowledge_level = data_from_csv[i][4]
            temp_student_instance.energy_level = data_from_csv[i][5]
            students.append(temp_student_instance)
        return students
