# python 3.5
# !/usr/bin/python
# -*- coding: latin-1 -*-


from TestQa.YouTube.Person import Person
from TestQa.YouTube.House import House

# обявление объекта класса
person1 = Person("John", 23)
person2 = Person("Mike", 34)

house = House()
house.set_address("1Street")

#person1.set_name("John")
#person1.set_age("23")
person1.set_address("New York")


#person2.set_name("Mike")
#person2.set_age("35")
person2.set_address("San Francisco")

house.settle_person(person1)
house.settle_person(person2)

person1.description_of_person()
person2.description_of_person()

house.description_of_house()
