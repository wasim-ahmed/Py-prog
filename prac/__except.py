class testexception(Exception): #handle the exception in your own way
	""" this is a user defined exception """
	
def check():
	try:
		num = int(input("Enter the number"))
		if num < 10:
			raise testexception #raise the exception due to some reason
	except testexception as e:
		print("Exception caught") #handle the exception in some more elegant manner
	else:
		print("all is well")
		return num	#return only when input value is correct
			
print(check())