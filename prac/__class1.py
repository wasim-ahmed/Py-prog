class base():
	def func(self,X1):
		X = X1
		print(X)
		
	def __str__(self):
		txt = "This is your object"
		return txt
		
class child(base):
	
	#def func(self,Z):
	#	print("in child class")
	
	def func1(self):
		print("inside child")
		#super().func(20)
		self.func(50) # via inheritance
#Bx = base()
#Bx.func(10)

Cx = child()
Cx.func1()
Bx = base()
print(Bx)