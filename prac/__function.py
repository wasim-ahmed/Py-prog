def area(radius):
	from math import pi
	return pi * radius * radius

	
def multi():
	a = 10
	b = 20
	return a,b
	
def list(*list): #prints the list
	for i in range(len(list)):
		print(list[i])
		
def dict(**dict):
	print(dict.keys())
	
	
def fact(n): #recursive function
	if n != 0:
		return n * fact(n-1)
	else:
		return 1


print(area(5))
a,b = multi()
print(a,b)
list([1,2,3,4,5])
Dx = {'one':1,'two':2}
dict(**Dx)

print(area.__name__)
print(area.__module__)
print(area.__code__)

print(fact(5))

product = lambda x = 10, y = 20 : x * y
print(product(3,2))

print(dir())