class Human:

    # properties/attributes
    height = 0
    weight = 0
    first_name = ""
    last_name = ""
    age = None
    level = 1
    asleep = False

    # methods
    def is_asleep(self):
        pass

    def is_hungry(self):
        pass

    def is_working(self):
        pass

    def level_up(self):
        if self.level < 100:
            self.level = self.level + 1
        else:
            print("Max level reached")


class Student(Human):  # inheritance

    major = None

    def is_studying(self):
        pass

