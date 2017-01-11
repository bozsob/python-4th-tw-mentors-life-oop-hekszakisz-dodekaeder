from person import Person
import random


class Kitchen():

    def __init__(self):
        self.coffee_amount = 100
        self.fridge_space = 2000
        self.phrases = [
            "Jönnek az arabok? Akkor kéne ide egy falra szerelhető kecske lyuk!", "Basszunk beljebb!!!",
            "Rendeljünk egy zsíroskenyér kenésű űrtalicskát!", "Kéne ide egy bicikli hajtású majomkenyérfa!"]

    def pakkos_phrases(self):
        print(
            "{} {}".format("Pakko felkiáltott:", random.choice(self.phrases)))

    def coffee_left(self, consumed_amount):
        self.coffee = self.coffee_amount - consumed_amount
        if self.coffee <= 0:
            print("Elfogyott a mana potion!!!")
            raise ValueError
        print(
            "{}{} {}".format("\n", self.coffee, "liter kávé maradt még.\n"))

    def fridge_space_left(self, food_amount):
        self.food = self.fridge_space - food_amount
        if self.food <= 0:
            print("\nNincs több hely a lembasz kenyérnek!")
            raise ValueError
        print(
            "{} {}".format(self.food, "köbdeci hely maradt még a hűtőben.\n"))

jani = Kitchen()
jani.coffee_left(5)
jani.fridge_space_left(60)
jani.pakkos_phrases()
