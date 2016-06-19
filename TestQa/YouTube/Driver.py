from TestQa.YouTube.Person import Person


class Driver(Person):
    __drive_exp = 0

    def set_drive_exp(self, dexp):
        self.__drive_exp = dexp

    def get_drive_exp(self):
        return self.__drive_exp

    def description_of_person(self):
        super().description_of_person()
        print("I am driver and my experience is", self.__drive_exp, "years")
