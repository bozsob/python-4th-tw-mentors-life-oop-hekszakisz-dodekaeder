from mentor import Mentor
from student import Student
from person import Person


class CodecoolClass:

    location = "Miskolc"
    year = 2016
    mentors = Mentor.create_by_csv()
    students = Student.create_by_csv()

    def __init__(self, location, year, mentors, students):
        self.location = str(location)
        self.year = int(year)
        self.mentors = mentors
        self.students = students

    @classmethod
    def generate_local(cls):
        print("\nMentors are initialized from CSV.")
        print("\nStudents are initialized from CSV.")
        print("\nSchool @ {}, in year {} is created, with {} mentors and {} students.".format(
            cls.location, cls.year, len(cls.mentors), len(cls.students)))

        return CodecoolClass(cls.location, cls.year, cls.mentors, cls.students)

    def find_student_by_full_name(self, full_name):

        for i in range(len(self.students)):
            if self.students[i].last_name + " " + self.students[i].first_name == full_name:
                print("\nIgen, '" + str(self.students[i]) +
                      "' megtalálható a tanulók között.")
                return self.students[i]
        print("\n")
        print("'" + full_name + "'" + " nevű tanuló nincs nálunk.")

    def find_mentor_by_full_name(self, full_name):

        for i in range(len(self.mentors)):
            if self.mentors[i].last_name + " " + self.mentors[i].first_name == full_name:
                print("\nIgen, '" + str(self.mentors[i]) +
                      "' megtalálható a mentorok között.")
                return self.mentors[i]
        print("\n")
        print("'" + full_name + "'" + " nevű mentor nincs nálunk.")
