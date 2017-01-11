from student import Student
import random


class Assignment:

    def __init__(self, name):
        self.name = name

    def grading_assignment(self, student):
        grade = (random.randint(1, 12)) * 3
        print(student + "\'s assignment has been graded. Your result is: ", grade)
        return grade

    def making_assignment(self, mentor):
        assignments_list = [
            "Nincs kedvem assignment-et írni, keressetek mást", "Zöldségek", "OOP", "Vegyigyümi"]
        result = random.choice(assignments_list)
        print("The mentor " + mentor + " did the following: " + result)

oop = Assignment("mentors oop")

oop.grading_assignment("Trx")
oop.making_assignment("Atesz")
