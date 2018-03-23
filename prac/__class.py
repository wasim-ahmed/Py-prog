#All Class member (including data members) are public & all methods are virtual.


class Test(object):
	""" This a test doc string """
	pass
	
Tx = Test()
print(Tx.__doc__)
print(isinstance(Tx,Test))
print(issubclass(Test,object))

Tx.var = 10

print(Tx.var)

print(Tx.__dict__)
#print(Tx.__name__)
print("-------------------------------------------------------")

# The variable outside the constructor are static variable and inside the constructor are object variable 
class shape():
	Var = 123
	def __init__(self):
		self.side1 = 5
		self.side2 = 4
	
	def area(self,S1,S2):
		self.side1 = S1
		self.side2 = S2
		area = self.side1 * self.side2
		return area
		
	def calc(self):
		X = 5
		return X
	

Sx = shape()
Ar = Sx.area(2,5)
print(Ar)
print(shape.Var) #static variable

print(Sx.__dict__)
