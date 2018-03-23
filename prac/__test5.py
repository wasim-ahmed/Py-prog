class A:
	def __init__(self):
		print("Base constructor")
		self.setme(10)
		print("value of i is",self.i)
		
		
	def setme(self,i):
		print("Base function")
		self.i = i + 10;
		
		
class B(A):
	def __init__(self):
		print("child constructor")
		super().__init__()
		
		
	def setme(self,i):
		print("child function")
		self.i = i + 20;
		
		
b = B()
'''
child constructor
Base constructor
child function
value of i is 30
'''