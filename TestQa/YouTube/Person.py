class Person:
    __name = "n/a"
    __age = 0

    def set_name(self, n):
        self.__name = n

    def set_age(self, a):
        self.__age = a

    #	def get_name(self):
    #		return self.__name

    #	def get_age(self):
    #		return self.__age

    def description_of_person(self):
        print("\n")
        print("Hi! My name is", self.__name)
        print("I am", self.__age, "years old")
