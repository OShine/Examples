# python 3.5
# !/usr/bin/python
# -*- coding: latin-1 -*-


from person import Person

# обявление объекта класса
person1 = Person()
person2 = Person()

person1.set_name("John")
person1.set_age("23")
person1.description_of_person()

person2.set_name("Mike")
person2.set_age("35")
person2.description_of_person()
