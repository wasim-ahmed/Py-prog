class Base:
	def __doit(self):
		return "Base"
		
	def printme(self):
		print(self.__doit())
		
class Sub(Base):
	def __doit(self):
		return "Sub"
		
def main():
	Base().printme() #Objects can be called from class name also
	Sub().printme()
	
main()