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

        for i in range(len(data_from_csv)):
            temp_mentor = Mentor()
            temp_mentor.first_name = data_from_csv[i][0]
            temp_mentor.last_name = data_from_csv[i][1]
            temp_mentor.year_of_birth = data_from_csv[i][2]
            temp_mentor.gender = data_from_csv[i][3]
            temp_mentor.nickname = data_from_csv[i][4]
            mentors.append(temp_mentor)
        return mentors
