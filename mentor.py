import csv
from person import Person


class Mentor(Person):

    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.year_of_birth = None
        self.gender = None
        self.nickname = None

    @classmethod
    def create_by_csv(cls, path="data/mentors.csv"):
        data_from_csv = []
        mentors = []
        with open(path, newline='') as myfile:
            for line in myfile:
                data_from_csv.append(line.strip().split(','))

        temp_mentor_instance = Mentor()
        for i in range(len(data_from_csv)):
            data_from_csv[i][0] = temp_mentor_instance.first_name
            data_from_csv[i][1] = temp_mentor_instance.last_name
            data_from_csv[i][2] = temp_mentor_instance.year_of_birth
            data_from_csv[i][3] = temp_mentor_instance.gender
            data_from_csv[i][4] = temp_mentor_instance.nickname
            mentors.append(temp_mentor_instance)
        return mentors

print(Mentor.create_by_csv())
