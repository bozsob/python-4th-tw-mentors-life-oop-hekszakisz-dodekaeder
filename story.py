from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from kitchen import Kitchen
from salary import Salary
from person import Person
from assignment import Assignment
from meeting import Meeting


codecool_msc2016 = CodecoolClass.generate_local()
codecool_msc2016.find_student_by_full_name("Vajnorák Zsolt")


def main():

    print(
        "\n\n" + '\033[1m' + "A csipet-csapat megérkezik a Codecoolba és jó szokásukhoz híven, a konyha felé veszik az irányt." + '\033[0m' + "\n")

    pakko = Kitchen()
    pakko.who_is_in_the_kitchen()
    print("\n" + pakko.student_in_kitchen +
          " neki áll vedelni a mogyorós kávét liter számra... Csak mert nem ő vette...")
    pakko.coffee_left(3)
    pakko.fridge_space_left(60)
    pakko.pakkos_phrases()

    print(
        "\n\n" +
            '\033[1m' +
                "És eljött vala az idő, hogy megtekintsük, mikor lesz a következő meeting és, hogy mi lesz a téma!" +
                    '\033[0m' + "\n"
    )

    peba = Meeting()
    peba.next_meeting()
    peba.topic_generator()
    print("\n\n" +
          '\033[1m' + "Miután lement a meeting, a mentoroknak eszükbe jutott, hogy fogytán a motiváció.\nMost átgondolják, hogy mikor fogja lehúzni róluk a nadrágot a sok della súlya újra. " + '\033[0m' + "\n")

    atesz = Salary(1)
    atesz.days_until_payday()
    atesz.warning_messages()

    print("\n\n" +
          '\033[1m' + "Most, hogy a motiváció a tetőfokára hágott, a kiadandó feladatokat is megbeszélik a mentorok." + '\033[0m' + "\n")

    imi = Assignment("Imre")
    imi.grading_assignment("Vajnorák Zsolt")
    imi.making_assignment()
    print("")
    pakko.pakkos_phrases()

    print("\n\n" +
          '\033[1m' + "Itt a móka vége mára, induljunk hát a kocsmába.\n")

if __name__ == "__main__":
    main()
