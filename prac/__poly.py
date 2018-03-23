class base:
	def test(self):
		print("base")
		
	def oreo(self):
		print("in base")
		self.test()#depends on the object which is calling

class child(base):
	def test(self):
		print("child")
		
	def org(self):
		print("in child")
		super().oreo()

Cx = child()
Cx.org()

print("-------------------------------------")

Bx = base()
Bx.oreo()

"""
Polymorphism depends through which object it is called
"""