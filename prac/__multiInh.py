class base1():
	def __init__(self):
		print("BASE1")
	def fun(self):
		print("in base1")

class base2():
	def __init__(self):
		print("BASE2")
	def fun(self):
		print("in base2")
		
class child(base1,base2): #depends on the order base1, base2
	def own(self):
		super().fun()
		
Cx = child()
Cx.own()