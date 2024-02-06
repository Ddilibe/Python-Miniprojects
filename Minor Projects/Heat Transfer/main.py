#!/usr/bin/env python3
""" Script for using object orientation for solving Heat Transfer Problem """
from math import pi, cosh


class TemperatureHeatTransfer(object):
	"""docstring for Temperature"""
	def __init__(self, **kwargs):
		super(TemperatureHeatTransfer, self).__init__()
		for key, value in kwargs.items():
			setattr(TemperatureHeatTransfer, key, value)

	def perimeter(self) -> float:
		""" Method for solving perimeter """
		score = {
			"circle": 2*pi*self.raduis,
			"rectangle": 2*(self.length + self.width),
			"square": 4*(self.length)
		}
		return score.get(self.shape)

	def area(self) -> float:
		""" Method for solving the area of the shape """
		score = {
			"circle": pi*(pow(self.raduis, 2)),
			"rectangle": self.length * self.width,
			"square": pow(self.length, 2)
		}
		return score.get(self.shape)

	def biot_number(self) -> float:
		""" Method for generating the biot number """
		numerator = self.heat_transfer_coefficient * self.perimeter()
		denorminator = self.thermal_conductivity * self.area()
		return (numerator/denorminator)**(1/2)

	def cosh_biot_number(self) -> float:
		""" Method for generating the cosh of the biot number """
		return cosh(self.biot_number())

	def numerator(self) -> float:
		""" Method for obtaining the numerator """
		return self.biot_temp_difference() * self.temp_difference()

	def biot_temp_difference(self) -> float:
		""" Method for generating the product of the biot number and the temperature
		difference """
		return self.cosh_biot_number()*(self.height-self.x)

	def denorminator(self) -> float:
		""" Method for obtaining the denorminator """
		return cosh(self.biot_number())*self.height

	def answer(self) -> float:
		""" Method for obtaining the final answer """
		side = self.numerator()/self.denorminator()
		return side + self.temp_ambient

	def temp_difference(self) -> float:
		""" Method to calculate the difference in temperature
		between the ambient temperature and the initial temperature
		of the extended body surface """
		return self.temp_initial-self.temp_ambient

if __name__ == '__main__':
	values_of_x = [0, 0.05, 0.1, 0.15, 0.20, 0.25, 0.3]
	cosh_biot_number, biot_temp_difference, denorminator, temp_initial = [], [], [], []
	temp_ambient, temp_difference, answer = [], [], []
	for i in values_of_x:
		variable = {
			"heat_transfer_coefficient" : 7.5,
			"thermal_conductivity": 43,
			"temp_ambient": 303,
			"temp_initial": 373,
			"raduis": 0.025/2,
			"shape": "circle",
			"height": 0.3,
			"length":0,
			"width":0,
			"x":i,
		}
		name = TemperatureHeatTransfer(**variable)
		print(f"""
			For the Values of {i},\n
			\t x : {name.x}\n
			\t cosh(b) : {name.cosh_biot_number()}\n
			\t cosh(b)(l-x) : {name.biot_temp_difference()}\n
			\t cosh(b)l : {name.denorminator()}\n
			\t To : {name.temp_initial}\n
			\t Ta: {name.temp_ambient}\n
			\t To - Ta: {name.temp_difference()}\n
			\t ans: {name.answer()}
		""")
		cosh_biot_number.append(name.cosh_biot_number())
		biot_temp_difference.append(name.biot_temp_difference())
		denorminator.append(name.denorminator())
		temp_initial.append(name.temp_initial)
		temp_ambient.append(name.temp_ambient) 
		temp_difference.append(name.temp_difference()) 
		answer.append(name.answer())
	print(f"{cosh_biot_number}, \n{biot_temp_difference}, \n{denorminator}, \n{temp_initial},\
				\n{temp_ambient}, \n{temp_difference}, \n{answer}"
		)