import pathlib 
import numpy as np

class Prototype:
	"""
		To start to solve the problem, we have to open the files first

		This class is specifically for opening the file and closing it after use

		Parameter
		File: File we are to open
		mode: Mode we would like to open the file
	"""
	def __init__(self, *args, **kwargs):
		""" Inintialzing the class to open the file. The class would be opening in initialzation """
		kwargs['file'] = pathlib.Path.home()/'Desktop'/'Python Projects'/'numpy'/'simplilearn'/'lesson 5'/'GDP dataset'/'Countries with GDP.txt'
		self._file = kwargs['file']
		# self._mode = mode
		self._openn = open(self._file,'r')

	def closing(self,):
		""" Method for closing the file """
		self._openn.close()

	def readlines(self,):
		""" Method for reading lines at different interval """
		return self._openn.readlines()

	def read(self,):
		""" Method to read the alphabe line by line """
		return self._openn.read()

class Assignment:
	"""
	 	This class is specifically used for starting the assignment given to me.

	 	It is going to call on the prototype function to open the while an record a number of things
	"""
	countries = []
	value = []
	countries_value = {} 
	def __init__(self,):
		"""Initializing the Assignment class """
		w = 0
		for i in Prototype().readlines():
			w+=1
			if w == 3:
				Assignment.countries = [x for x in i.split(',')]
			if w == 8:
				Assignment.value = [float(x) for x in i.split(',')]
		print(f"{Assignment.countries} \n {Assignment.value}")
		self.mergjo()
		print(Assignment.countries_value)
		self._as = np.array(Assignment.value)
		print(f"\n\n{self._as}")
		self.details()
		self.answer()

	def splito(self, com, show):
		""" Method for suppling the dataset with data"""
		com = com.split(',')
		for i in com:
			try:
				show.append(int(i))
			except ValueError as e:
				print(ValueError)
			else:
				show.append(str(i))

	def mergjo(self,):
		"""Method for supplying the countries_value with data"""
		for i in range(len(Assignment.value)):
			Assignment.countries_value[Assignment.countries[i]] = Assignment.value[i]

	def finto(self, world):
		""" Method is for iterating over somethings and picking the correct answer"""
		for value in Assignment.countries_value:
			if world == Assignment.countries_value[value]:
				break
		return value

	def answer(self,):
		"""Method to display the assignment"""
		x = self._as.max()
		h = self.finto(x)
		print(f"The country with the highest GDP is {h} with a GDP of {Assignment.countries_value.get(h)}")
		x = self._as.min()
		h = self.finto(x)
		print(f"The country with the lowest GDP is {h} with a GDP of {Assignment.countries_value.get(h)}")
		print(f"The mean is {self._as.mean()}. The sum of all the dataset is {self._as.sum()}. The highes value is {self._as.max()}. The lowest value is {self._as.min()}")

	def details(self,):
		""" Method for printing out text and input values iteratively"""
		for i in Assignment.countries_value:
			print(i)
		for i in Assignment.countries_value:
			print(Assignment.countries_value[i])
		""" Method to print an entire list of countries with their GDP"""
		for i,r in Assignment.countries_value.items():
			print(f"{i}		: 	{r}")

if __name__ == "__main__":
	Assignment()