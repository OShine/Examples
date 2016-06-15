from TestQa.YouTube.Person import *


class House:
    __address = "n/a"
    __list_of_residents = ["n/a"]

    def set_address(self, a):
        self.__address = a

    def get_address(self):
        return self.__address

    def settle_person(self, p):
        if isinstance(p, Person):
            self.__list_of_residents.append(p)
            p.set_address(self.__address)

    def evict_person(self, p):
        self.__list_of_residents.remove(p)
        p.set_address("n/a")

    def description_of_house(self):
        print("\n")
        print("Address of this house is: ", self.__address)
        print("List of residents:")
        for p in self.__list_of_residents:
            if isinstance(p, Person):
                print("# -", p.get_name())
