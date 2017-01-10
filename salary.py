import datetime


class Salary:

    def __init__(self, pay_day):
        self.pay_day = pay_day
        if self.pay_day > 31:
            print("Days can\'t be greater than 31 days.")
            return ValueError
        self.now = datetime.date.today()
        self.year = self.now.year
        self.month = self.now.month + 1
        self.pay_date = datetime.date(self.year, self.month, self.pay_day)

    def days_until_payday(self):
        if self.pay_date == self.now:
            print("\nToday is the golden day mate!!")
        else:
            print("\nNext pay date is " + str(self.pay_date) + ". " + str(abs(self.pay_date - self.now)
                                                                          .days) + " days left for the next salary.\n")

jani = Salary(5)
jani.days_until_payday()
