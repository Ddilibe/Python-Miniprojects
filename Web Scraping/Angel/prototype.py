import requests
from abc import abstractmethod, ABCMeta
from bs4 import BeautifulSoup

class Prototype():
	"""
		This class is specifically for design a prototyoe for designing the web scraping tool used to build angel's media
	"""
	list_developed = [] #List of websites developed
	self_generated_items = []
	def __init__(self, website, parenttag, tag, title):
		""" 
			Initializing the request from the main class.

			Input Parameters
			website = "https://www.wikipedia.com"
			parenttag = 'h1'
			tag = "class"
			title = 'name_attributed_to_tag'
		"""
		self._website = website
		self._response = requests.get(self._website)
		self._soup = BeautifulSoup(self._response.content, "html.parser")
		self._reason = self._soup.find(tag)
		# Parsing through the website to get a set of links to a tag
		Prototype.list_developed = [i for i in self._reason]
		self.generate_things()

	@abstractmethod
	def generate_things(self,):
		""" Method that each class can used to develop its own version of a data base """
		pass	

	@abstractmethod
	def return_list(self,):
		""" Method used to return a class generated list of items for the webpage """
		return Prototype.self_generated_items

	def __str__(self,):
		""" Giving meaning to the generated class """
		return f"Webscraper for the website ({self._website})"