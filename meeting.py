import random
import datetime


class Meeting:

    def __init__(self):
        self.now = datetime.datetime.now()
        self.time = datetime.time(self.now.hour, self.now.minute)

        self.topics = ["Retrospektív",
                       "Új kurzus",
                       "Karácsonyi buli",
                       "Hol ebédeljünk?",
                       "Helyi Mortal Kombat bajnokság",
                       "Fürdés a sok pénzben",
                       "Az élet értelme",
                       "Oktatási menetrend",
                       "Világuralom!"]

    hours = [15, 16, 17, 18, 19]
    h = random.choice(hours)
    mins = [00, 15, 30, 45]
    s = random.choice(mins)
    meeting_time = datetime.time(h, s)

    def next_meeting(self):
        meeting_time = self.meeting_time
        current_time = self.time
        remaining = datetime.datetime.combine(datetime.date.today(), meeting_time) - \
            datetime.datetime.combine(datetime.date.today(), current_time)
        if remaining < datetime.timedelta(0, 0, 0):
            print("\nMára nincs több megbeszéleés.")
            return
        else:
            print("\nA következő megbeszélés " +
                  str(abs(remaining)) + " múlva lesz.")
            return

    def topic_generator(self):
        topic = random.choice(self.topics)
        result = "\nA következő téma: " + topic
        print(result)
        return result
