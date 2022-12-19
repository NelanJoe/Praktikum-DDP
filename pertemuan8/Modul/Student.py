# from Person import *
from Modul.Person import Person

# Extend :=> nurunin sifat dari class Person
class Student(Person):
    # Manggil constructor class Person
    def __init__(self, name, address, age, nim, jurusan):
        super().__init__(name, address, age)
        self.nim = nim
        self.jurusan = jurusan