class Node:

	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(sef, newnext):
		self.next = newnext

class UnorderedList:

	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		count = 0
		current = self.head

		while current != None:
			count += 1
			current = current.getNext()

		return count

if __name__ == '__main__':
	node = Node(12)
	print(node.getData())