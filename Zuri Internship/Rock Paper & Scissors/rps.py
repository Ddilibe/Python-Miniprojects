#!/usr/bin/python3
import random


class RockPaperScissors:

	RPS = ("R", "P", "S")
	RPSDictionary = {
		"R": "Rock",
		"P": "Paper",
		"S": "Scissors"
	}

	def __init__(self,):
		print("The weapon are\n \"R\" for Rock\n"
				" \"P\" for Paper\n"
				" \"S\" for Scissors\nPick your weapon: ", end="")
		player = input("")
		computer = random.choice(RockPaperScissors.RPS)
		self._player = player
		self._computer = computer
		if self.check_player() is False:
			self.minor_information(1)
			self.__init__()
		else:
			self.Main()

	def check_player(self):
		""" Method to verify that the inputed variable is a weapon
		in the rock, paper and scissors game. """
		if self._player.upper() not in RockPaperScissors.RPS:
			return False

	def minor_information(self, number):
		""" Method is for displaying any information """
		if number == 1:
			print(f"\nThe selected weapon {self._player}, is "
					"not among the weapons\nPls, Input a correct weapon")
		if number == 2:
			print("\nIt is a tie. So you start again\n")
		if number == 3:
			print(f"Player({RockPaperScissors.RPSDictionary[self._player]}) : "
			      f"CPU({RockPaperScissors.RPSDictionary[self._computer]})")

	def attack_mode(self,):
		"""
		Method to determine whether one of the computer won or the player

		The first conditional is for the computer
		The second conditional is for the player attack
		The final conditional is for a tie.
		"""
		if self.attack(self._computer, self._player):
			return 1
		elif self.attack(self._player, self._computer):
			return 2
		else:
			return 0

	def attack(self, comp, play):
		""" Method to attack the computer and the player. """
		if comp == "R" and play == "S":
			return True
		elif comp == "P" and play == "R":
			return True
		elif comp == "S" and play == "P":
			return True
		else:
			return False

	def Main(self, ):
		"""
		Method to launch the Rock Paper Scissors game
		"""
		score = self.attack_mode()
		self.minor_information(3)
		if score == 1:
			self.winner("computer")
		if score == 2:
			self.winner("Player")
		if score == 0:
			self.minor_information(2)
			self.__init__()

	def winner(self, A):
		""" Method for printing the Winners in the rock, paper and scissors game """
		print(f"{A} Wins")

	def __str__(self,):
		""" The string built-in method """
		return ("A Rock Paper Scissors Game")


if __name__ == '__main__':
	RockPaperScissors()
