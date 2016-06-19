from TestQa.YouTube.Person import Person


class Programmer(Person):
    __programmer_exp = 0

    def set_programmer_exp(self, pex):
        self.__programmer_exp = pex

    def get_programmer_exp(self):
        return self.__programmer_exp

    def description_of_person(self):
        super().description_of_person()
        print("I am programmer and my experience is", self.__programmer_exp, "years")