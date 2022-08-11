from random import randint

class myIterable:
	def __init__(self,n):
		self.n = n
	def __iter__(self):
		return myIterator(self.n)

class myIterator:
	def __init__(self,n):
		self.cnt = 0
		self.n = n
	def __iter__(self):
		return self
	def __next__(self):
		if self.cnt < self.n:
			self.cnt += 1
			return randint(1,100)
		else:
			raise StopIteration
'''
try:
	able = myIterable(3)
	it = iter(able)
	print(next(it))
	print(next(it))
	print(next(it))
	print(next(it))
except Exception as e:
	print(repr(e))
'''

for i in myIterable(3):
	print(i)	



