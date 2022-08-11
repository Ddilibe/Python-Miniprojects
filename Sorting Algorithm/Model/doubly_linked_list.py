


class Node:
	""" The node of a class of a doubly linked list
	"""
	def __init__(self, data, prev=None, next=None):
		""" Initiation class of the doubly linked list """
		self.data = data
		self.next = next
		self.prev = prev


class DoublyLinkedList:
	""" Class that represents the doubly linked list
	"""
	def __init__(self, head=None):
		""" instantiazing the doubly linked list """
		self.head = head

	def add_at_end(self, value):
		""" Method to add data at the end of the linked list """
		if not isinstance(self.head, Node):
			self.head = Node(value)
		else:
			new = self.head
			them = new
			while(new is not None):
				them = new
				new = new.next
			first = Node(value)
			them.next = first
			first.prev = them

	def display(self):
		""" Method for displaying contents of a linked list """
		if isinstance(self.head, Node):
			new_list = self.head
			while new_list != None:
				print(new_list.data)
				new_list = new_list.next

	def add_at_beginning(self, value):
		""" Method to add element at the beginning of the doubly linked list """
		if not isinstance(self.head, Node):
			self.head = Node(value)
		else:
			new = self.head
			self.head = Node(value)
			self.head.next = new
			new.prev = self.head

	def add_at_index(self, value, index):
		""" Method to add element at the index in the doubly linked list"""
		if isinstance(self.head, Node):
			i = 0
			new = self.head
			while new != None:
				if i == index:
					old = Node(value)
					old.next = new.next
					old.prev = new
					new.next.prev = old
					new.next = old
					return 
				new = new.next
				i += 1
			raise IndexError(" Index larger than length of linked list")
		else:
			self.head = Node(value)

	@classmethod
	def next(cls):
		return cls.

if __name__ == '__main__':
	w = DoublyLinkedList()
	for i in range(10, 100, 9):
		w.add_at_end(i)
	for i in range(100, 1000, 73):
		w.add_at_beginning(i)
	w.add_at_index(234, 0)
	w.add_at_index(234, 3)
	w.add_at_index(234, 4)
	w.add_at_index(234, 2)
	w.add_at_index(234, 6)
	w.display()
	w.add_at_index(234, 76)