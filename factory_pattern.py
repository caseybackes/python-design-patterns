# import the abstract meta class from built-in abc library as well as
# the abstractstaticmethod
from abc import ABCMeta, abstractstaticmethod

# We create an abstract person class. As this is an interface class
class IPerson(metaclass=ABCMeta):
	@abstractstaticmethod
	def person_method():
		""" Interface Method """

class Student(IPerson):
	def __init__(self):
		self.name = "Student Name"
	
	def person_method(self):
		print("I am a student")

class Teacher(IPerson):
	def __init__(self):
		self.name = "Teacher Name"
	def person_method(self):
		print("I am a teacher")


class PersonFactory:
	@staticmethod
	def build_person(person_type):
		if person_type == "Student":
			return Student()
		if person_type == "Teacher":
			return Teacher()
		print("Invalid Type")
		return -1

if __name__ == "__main__":
	choice = input("What type of person do you want to create?\n")
	person = PersonFactory.build_person(choice)
	person.person_method()



