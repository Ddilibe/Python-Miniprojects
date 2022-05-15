from scipy import linalg
import numpy as np

"""
	A script to solve a linear equation of a number of unknowns. We will be
	solving this problem with scipy using the gausian elimination method

	Instructions:
	1. Import required libraries
	2. Formulate two linear equations based on the given scenario
	3. Apply a suitable method to solve the linear equation
	
	Equation attempting to solve
		39A + 27B - 49C + 27D + 49E = 28
		-32A - 90B + 59C - 12D + 23E = 23
		93A - 37B - 20C + 20D - 76E = 75
		14A + 38B - 02C + 34D - 64E = 45
		-88A + 32B - 38C + 39D + 35E = 78
"""

equation = np.array([[39,27,-49,-27,49],[-32,-90,59,-12,23],[93,-37,-20,20,76],[14,38,2,34,64],[-88,32,-38,39,35]])
answers = np.array([28,23,75,45,78])
unknowns = ['A','B','C','D','E']
solution = linalg.solve(equation, answers)
for i in range(0,5):
	print(f"{unknowns[i]}:{solution[i]}")