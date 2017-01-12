from mentor import Mentor
from student import Student
import random


class Kitchen():

    def __init__(self):
        self.coffee_amount = 20
        self.fridge_space = 200
        self.mentor_in_kitchen = str(
            Mentor.create_by_csv()[random.randint(0, 4)])
        self.student_in_kitchen = str(
            Student.create_by_csv()[random.randint(0, 2)])
        self.phrases = [
            "Jönnek az arabok? Akkor kéne ide egy falra szerelhető kecske lyuk!", "Basszunk beljebb!!!",
            "Rendeljünk egy zsíroskenyér kenésű csúszó űrtalicskát!", "Kéne ide egy bicikli hajtású majomkenyérfa!", "Készítsünk koszos zokni ízű sört!"]

    def who_is_in_the_kitchen(self):
        if self.mentor_in_kitchen != "Monoczki Pál":
            print("\nA konyhában a következő személyek vannak:\nMentor: " +
                  str(self.mentor_in_kitchen) + ", Pakko" + "\nCodecoolerek: " + str(self.student_in_kitchen))
        else:
            print("\nA konyhában a következő személyek vannak:\nMentor: " +
                  str(self.mentor_in_kitchen) + "\nCodecoolerek: " + str(self.student_in_kitchen))

    def pakkos_phrases(self):
        print(
            "{} {}".format("Pakko felkiáltott:", random.choice(self.phrases)))

    def coffee_left(self, consumed_amount):
        self.coffee = self.coffee_amount - consumed_amount
        if self.coffee <= 0:
            print("\nElfogyott a mana potion!!!\n")
            raise ValueError
        print(
            "{}{} {} {} {} {}".format("\n", self.student_in_kitchen, consumed_amount, "liter kávét betolt, ", self.coffee, "liter kávé maradt még.\n"))

    def fridge_space_left(self, food_amount):
        self.food = self.fridge_space - food_amount
        if self.food <= 0:
            print("\nNincs több hely a lembasz kenyérnek!\n")
            raise ValueError
        print(
            "{} {} {} {} {}".format(self.student_in_kitchen, food_amount, "köbdeci ételt a hűtőbe rakott, ", self.food, "liter hely maradt még a hűtőben.\n"))
