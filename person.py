class Person:

    def __init__(self, first_name, last_name, year_of_birth, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        if gender in ("male", "female", "not sure"):
            continue
        else:
            raise AttributeError

    def __str__(self, person):
        return (self.last_name + " " + self.first_name)
