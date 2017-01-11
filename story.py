from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from kitchen import Kitchen
from salary import Salary
from person import Person
from assignment import Assignment


codecool_msc2016 = CodecoolClass.create_local


def main():

    robi = Salary(5)
    robi.days_until_payday()
    robi.warning_messages()


if __name__ == "__main__":
    main()
