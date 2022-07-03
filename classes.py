# University endowment per student calculation using classes
class University:
	'''
	Creating a class which will hold university instances and a method.
	'''
	def __init__(self, name, endowment, students):
		self.name = name
		self.endowment = endowment
		self.students = students

	def endowment_per_student(self):
		return self.endowment//self.students

AU = University(name='American University', endowment=884305000, students=14318)
Harvard = University(name='Harvard University', endowment=53200000000, students=22947)

print(f'{AU.name} has ${AU.endowment_per_student()} of endowment money per student.')
print(f'{Harvard.name} has ${Harvard.endowment_per_student()} of endowment money per student.')
