from doubly_linked_list import DoublyLinkedList, Node



def main():
	""" The main function to test the insertion algorithm """

	new_list = [571, 77, 267, 385, 340, 868, 694, 919, 721, 67]
	w = InsertionSortAlgorithm()
	for i in new_list:
		w.add_at_end(i)
	print("Before the insertion sort")
	w.display()
	w.insertion_sort()
	print("After the insertion sort")
	w.display()
	return


class InsertionSortAlgorithm(DoublyLinkedList):
	"""
		Class for all the sorting algorithm to be used in Python
	"""

	def insertion_sort(self):
		""" Method for implementing the insertion sort algorithm """
		them = self.head
		while(them != None):
			this = them.next
			some = them
			while(this != None):
				if some.data > this.data:
					dude, card = some, this
					some.prev = card.prev
					some.next = card.next
					this.prev = dude.prev
					this.next = dude.next
					if dude.next:
						dude.next.prev = this
					if dude.prev:
						dude.prev.next = this
					if card.prev:
						card.prev.next = some
					if card.next:
						card.next.prev = some
				# if some.data > this.data:
				# 	print("\n\n")
				# 	if some.prev:
				# 		some.prev.next = this
				# 		this.prev = some.prev
				# 	else:
				# 		this.prev = None
				# 	if this.next:
				# 		this.next.prev = some
				# 		some.next = this.next
				# 	else:
				# 		some.next = None
				# 	this.next = some.next
				# 	self.display()
				this = this.next
			them = them.next

# def insertion_sort(self, some):
# 	if isinstance(some, DoublyLinkedList):

# 	raise SyntaxError(" This class is not an instance of the doubly linked List")
if __name__ == '__main__':
	main()