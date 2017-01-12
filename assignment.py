from student import Student
from codecool_class import CodecoolClass
import random


class Assignment:

    def __init__(self, mentor):
        self.mentor = mentor

    def grading_assignment(self, student):
        students = Student.create_by_csv()
        grade = None

        for i in range(len(students)):
            if student == students[i].last_name + " " + students[i].first_name:
                print("A codecooler írt Assignment-et.")

                grade = (random.randint(1, 12)) * 3
                print(
                    student + " Assignment-jét értékelték, az eredménye: " + str(grade) + " pont")
                if grade > 25:
                    students[i].knowledge_level = 100
                    print(
                        student + " tudásszintje egekbe emelkedett, az értéke: " + str(students[i].knowledge_level))
                else:
                    students[i].knowledge_level = 1
                    print(
                        student + " tudásszintje csak sétálgat felfelé. Tanuljon többet!")

        return grade

    def making_assignment(self):
        assignments_list = [
            "Nincs kedvem assignment-et írni, keressetek mást.", "Zöldségek", "OOP - Orbitális Otthoni Palacsinta", "Vegyigyümi"]
        result = random.choice(assignments_list)
        print("Mentor a következő Assignment-et írta: " + result)

atesz = Assignment("Molnár Attila")

atesz.grading_assignment("Bozsó Beatrix")
atesz.making_assignment()
