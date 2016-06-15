class Person:
    __name = "n/a"
    __age = 0
    __address = "n/a"

    def __init__(self, n, a):
        self.__name = n
        self.__age = a

    def set_name(self, n):
        self.__name = n

    def set_age(self, a):
        self.__age = a

    def set_address(self, a):
        self.__address = a

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address

    def description_of_person(self):
        print("Hi! My name is", self.__name)
        print("I am", self.__age, "years old")
        print("My address is", self.__address, "")
        print("\n")

    @staticmethod
    def testStatic():
        print("I am static method")

    @classmethod
    def testClass(cls):
        print("I am class method")
        print(cls.__age)