# python 3.5
# !/usr/bin/python
# -*- coding: latin-1 -*-


from TestQa.YouTube.Person import Person
from TestQa.YouTube.House import House
from TestQa.YouTube.Programmer import Programmer
from TestQa.YouTube.Driver import Driver


# обявление объекта класса
person1 = Person("John", 23)
person2 = Programmer("Mike", 34)
person3 = Driver("Dave", 25)
house = House("2nd Street")

person1.set_address("New York")
person2.set_address("San Francisco")
person3.set_address("New Jersey")

person2.set_programmer_exp(3)
person3.set_drive_exp(5)

house.settle_person(person1)
house.settle_person(person2)

person1.description_of_person()
person2.description_of_person()
person3.description_of_person()

house.description_of_house()
