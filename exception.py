
it = iter([1,2,3,4,5])	

try:	
	print(next(it))	
	print(next(it))	
	print(next(it))	
	print(next(it))	
	print(next(it))	
	print(next(it))	
except Exception as e:
	print(repr(e))
	
