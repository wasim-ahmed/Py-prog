class A:
	var1 = 5
	def __init__(self,i=0):
		self.i = i
		print("inside A")
		self.X2 = 100
		X3 = 500
		
	def test(self):
		self.X1 = 10
		X5 = 120
		print("in the base test function",X5)
		
class B(A):
	def __init__(self,j=0):
		self.j = j
		print("inside B")
		a = A()
		print(a.X2) #variables of base class are accessible from derived class functions/constructor
		#print(a.X3)
		#super().__init__() # Base class constructor is not called automatically you need to call it explicitly using super keyword 
		
def main():
	b = B()
	#print(b.i) #Error
	print(b.j)
	print(b.test())
	print(b.var1)
	print(b.X1) 
	#print(b.X5) #this is local to class and will not be accessible from B as it is not given by self
	#print(b.X2) #variables inside the constructor are sort of private to class and are not accessible from child class object
	
main()

#So a variable as to be declared through "self." in order to be accessible from derived class
#variables in constructor are not accessible outside to derived class 