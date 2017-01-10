import csv
from person import Person


class Mentor(Person):

    def __init__(self, nickname):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.nickname = nickname

    @classmethod
    def create_by_csv(cls, path):
        data_from_csv = []
        mentors = []

        with open(path, newline='') as myfile:
            for line in myfile:
                data_from_csv.append(line.strip().split(','))

        return data_from_csv
