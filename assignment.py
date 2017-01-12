from student import Student
from codecool_class import CodecoolClass
import random


class Assignment:

    def __init__(self, name):
        self.name = name

    def grading_assignment(self, student):

        if CodecoolClass.find_student_by_full_name(self, student):

            grade = (random.randint(1, 12)) * 3
            print(student + " Assignment-jét értékelték, az eredménye: " +
                  str(grade) + " pont")
        if grade > 25:
            Student.knowledge_level += 5
            print(student + " tudásszintje egekbe emelkedett, az értéke: " +
                  Student.knowledge_level)
        return grade

    def making_assignment(self, mentor):
        assignments_list = [
            "Nincs kedvem assignment-et írni, keressetek mást.", "Zöldségek", "OOP - Orbitális Otthoni Palacsinta", "Vegyigyümi"]
        result = random.choice(assignments_list)
        print("Mentor " + mentor + " a következő Assignment-et írta: " + result)

oop = Assignment("mentors oop")

oop.grading_assignment("Trx")
oop.making_assignment("Atesz")
