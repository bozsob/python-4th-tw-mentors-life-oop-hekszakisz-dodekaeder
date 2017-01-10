from person import Person
import csv


class Student(Person):
    Try:
        def __init__(self, first_name, last_name, year_of_birth, gender, knowledge_level, energy_level):
            super().__init__(self, first_name, last_name, year_of_birth, gender)
            self.knowledge_level = knowledge_level
            self.energy_level = energy_level

        @staticmethod
        def create_by_csv(path):
            students = []
            with open(path, newline="") as data:
                for line in data:
                    students.append(line.strip().split(","))
            return students

    except:
        raise ValueError
