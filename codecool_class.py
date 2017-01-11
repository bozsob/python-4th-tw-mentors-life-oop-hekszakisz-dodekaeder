from mentor import Mentor
from student import Student


class CodecoolClass:

    def __init__(self, location, year, mentors, students):
        self.location = location
        self.year = year
        self.mentors = mentors
        self.students = students

    @classmethod
    def generate_local(cls):
        print("Mentors are initialized from CSV")
        print("Students are initialized from CSV")
        print("School @ " + location + ", in year " + year + " is created, with " +
              len(mentors) + " mentors and " + len(students) + " students.")

        return CodecoolClass(location, year, mentors, students)

    def find_student_by_full_name(full_name):
