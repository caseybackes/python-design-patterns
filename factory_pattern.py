'''
The Factory Method Design Pattern

The central idea in Factory Method is to provide 
a separate component with the responsibility to decide 
which concrete implementation should be used based on 
some specified parameter. 

In this exercise, that parameter is "person_type" - ie: "Student" or "Teacher".
A different class will be created by the factory class depending on this parameter.
'''


# import the abstract base class('abc') from built-in abc library as well as
# the abstractstaticmethod (implemented only on concreate instances inherited
# from the interface abstract class). 
from abc import ABCMeta, abstractstaticmethod

# We create an abstract person class. We use this to build
# specific person classes. Here, we define any mandatory methods that must
# be defined by any concrete implementations of this abstract (interface) class.
class IPerson(metaclass=ABCMeta):
	# Each 'person' class will have to have a 'person_method'.
	# We do not define what that method does in this interface,
	# simply that is must exist when a concrete implementation of the 
	# person class is instantiated. 
	# We do not instanstiate an abstract class, but rather use it 
	# as a baseline blueprint of a more concrete instance ("Student", "Teacher"). 
	# Abstract static methods take no arguments and do not access or have 
	# knowledge about its class or any instance of that class. Hence, 
	# no arguments.  
	@abstractstaticmethod
	def person_method():
		""" Interface Method """ # to be defined in concreate instances.

'''
We create a specific person class "Student" that inherits from 
the abstract IPerson class. In so doing, we must overwrite 
the 'person_method' inherited from IPerson to make it a 
concreate implementation of the IPerson abstract class. This is 
why the 'person_method' is not fully defined in the interface: 
it will vary depending on the classes that inherit from IPerson.
'''
class Student(IPerson):
	# Constructor: 
	def __init__(self):
		self.name = "Student Name"
	# Override the 'person_method' 
	def person_method(self):
		print("I am a student")

class Teacher(IPerson):
	def __init__(self):
		self.name = "Teacher Name"
	def person_method(self):
		print("I am a teacher")

'''
The Factory design pattern is where the bifurcation occurs between 
abstract and concrete instances. The purpose of the factory class 
(whatever the class name) is to create classes of objects based on 
some parameter (here, the type of person: Teacher or Student). 
'''
class PersonFactory:
	# Define a method that creates different classes based on the
	# 'person_type' parameter. We do not need to access any information
	# about a particular instance or the class, simply create a 
	# utility function. 
	@staticmethod
	def build_person(person_type):
		if person_type == "Student":
			return Student()
		if person_type == "Teacher":
			return Teacher()
		# if the person type does not match at this point, the
		# input was invalid. 
		print("Invalid Type")
		return -1

if __name__ == "__main__":
	choice = input("What type of person do you want to create?\n")
	person = PersonFactory.build_person(choice)
	person.person_method()



