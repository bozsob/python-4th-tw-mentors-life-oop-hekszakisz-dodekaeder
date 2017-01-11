import csv
from person import Person


class Mentor(Person):

    def __init__(self, nickname):
        super().__init__(first_name, last_name, year_of_birth, gender)
        self.nickname = nickname

    @classmethod
    def create_by_csv(cls, path):
        mentors = []

        with open(path, newline='') as myfile:
            for line in myfile:
                mentors.append(line.strip().split(','))

        return mentors
