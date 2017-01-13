import datetime


class Salary:

    def __init__(self, pay_day):
        self.pay_day = pay_day
        if self.pay_day > 31 or self.pay_day < 1:
            print(
                "\nNem adhatsz meg több napot, mint 31 nap illetve kevesebbet, mint 1 nap!\n")
            raise ValueError
        self.now = datetime.date.today()
        self.year = self.now.year
        self.month = self.now.month + 1
        self.pay_date = datetime.date(self.year, self.month, self.pay_day)

    def days_until_payday(self):
        if self.pay_date == self.now:
            print(
                "\nAranyeső a szép kis házra... Fizetésnap és halál a májra!!\n")
        else:
            print("\nA következő fizetés dátuma: " + str(self.pay_date) + ". " + str(abs(self.pay_date - self.now)
                                                                                     .days) + " nap van még hátra a következő fizetésig.\n")

    def warning_messages(self):
        if (self.pay_date - self.now).days >= 5 and (self.pay_date - self.now).days < 10:
            print("\nHabzsi-dőzsi van kispajtás!!! Basszál beljebb!!\n")
        if (self.pay_date - self.now).days >= 10 and (self.pay_date - self.now).days < 20:
            print("\nLassan vegyél vissza a sörikéből komám!\n")
        if (self.pay_date - self.now).days < 10 and (self.pay_date - self.now).days > 5:
            print(
                "\nNa most már nincs itt ilyen luxus, mint a Fapados vagy a Batyutéka!! Egyél szépen májkrémes kenyeret!\n")
        if (self.pay_date - self.now).days <= 5:
            print(
                "\nSzáraz a kenyér bástya? Sebaj, jó az még pirítósnak! Meleg vízzel meg csak a gyengék tusolnak!\n")
