def double(function):
	def wrapper(*args,**kwargs):
		return 2 * function(*args,**kwargs)
	return wrapper

@double
def adder(x,y):
	return x + y

print(adder(1,3))