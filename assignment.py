from mentor import Mentor
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
                print(
                    "\nÉs most lássuk, hogy " + student + " írt-e assignmentet! \nA codecooler írt Assignment-et.")

                grade = (random.randint(1, 12)) * 3
                print("\n" +
                      student + " Assignment-jét értékelték, az eredménye: " + str(grade) + " pont")
                if grade > 25:
                    students[i].knowledge_level = 100
                    print("\n" +
                          student + " tudásszintje egekbe emelkedett, az értéke: " + str(students[i].knowledge_level))
                else:
                    students[i].knowledge_level = 1
                    print("\n" +
                          student + " tudásszintje csak sétálgat felfelé. Tanuljon többet!")

        return grade

    def making_assignment(self):
        assignments_list = [
            "Nincs kedvem assignment-et írni, keressetek mást.", "Zöldségek", "OOP - Orbitális Otthoni Palacsinta", "Vegyigyümi"]
        result = random.choice(assignments_list)

        print("\n" + str(
            Mentor.create_by_csv()[random.randint(0, 4)]) + " a következő Assignment-et írta: " + result)
