import datetime


class Salary:

    def __init__(self, pay_day):
        self.pay_day = pay_day
        if self.pay_day > 31:
            print("Days can\'t be greater than 31 days.")
            raise ValueError
        self.now = datetime.date.today()
        self.year = self.now.year
        self.month = self.now.month + 1
        self.pay_date = datetime.date(self.year, self.month, self.pay_day)

    def days_until_payday(self):
        if self.pay_date == self.now:
            print("\nToday is the golden day mate!!")
        else:
            print("\nA következő fizetés dátuma: " + str(self.pay_date) + ". " + str(abs(self.pay_date - self.now)
                                                                                     .days) + " nap van még hátra a következő fizetésig.\n")

    def warning_messages(self):
        if abs(self.pay_date - self.now).days >= 5:
            print("\nHabzsi-dőzsi van kispajtás!!! Basszál beljebb!!\n")
        if abs(self.pay_date - self.now).days >= 10 and abs(self.pay_date - self.now).days < 20:
            print("\nLassan vegyél vissza a sörikéből komám!\n")
        if abs(self.pay_date - self.now).days < 10 and abs(self.pay_date - self.now).days > 5:
            print(
                "\nNa most már nincs itt ilyen luxus, mint a Fapados vagy a Batyutéka!! Egyél szépen májkrémes kenyeret!\n")
        if abs(self.pay_date - self.now).days <= 5:
            print(
                "\nSzáraz a kenyér bástya? Sebaj, jó az még pirítósnak! Meleg vízzel meg csak a gyengék tusolnak!\n")
