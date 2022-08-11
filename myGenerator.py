from random import randint

def myGenerator(n):
	cnt = 0
	while cnt < n:
		yield randint(1,100)
		cnt += 1

g = myGenerator(5)
print(g)	

#Generator comprehension	
g = (randint(1,100) for _ in range(5))
print(g)	
