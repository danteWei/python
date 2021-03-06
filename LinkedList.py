class LinkedList:
	def __init__(self):
		self.length = 0
		self.head   = None

	def addFirst(self, cargo):
		node = Node(cargo)
		node.next = self.head
		self.head = node
		self.length = self.length + 1

class Node:
	def __init__(self, cargo=None, next=None):
		self.cargo = cargo
		self.next  = next

	def __str__(self):
		return str(self.cargo)

	def print_list(node):
		print "[",
		while node:
			if isinstance(node.cargo, LinkedList):
				Node.print_list(node.cargo.head)
			else:
				print node,
			node = node.next
		print "]",
