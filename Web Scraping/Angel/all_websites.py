from prototype import Prototype

class PunchNgUrl(Prototype):
	"""
		Class for gathering the necessary urls from Punchng website
	"""
	collected_url = [] #List of websites developed
	def __init__(self, website, parenttag, tag, title):
		""" Initializing the super class of the PunchNgUrl """
		super().__init__(website, parenttag, tag, title)

	def generate_things(self,):
		""" Method that each class can used to develop its own version of a data base """
		for i in PunchNgUrl.list_developed:
		    y = i.find('a')
		    PunchNgUrl.collected_url.append(y['href'])

