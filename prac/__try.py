#import exceptions
def div(n):
	if n == 0:
		raise ZeroDivisionError
	else:
		return (10/n)
		
div(2)
try:
	Fd = open("abcd.io",'r')
except IOError:
	print("File does not exist")
finally:
	print("I will always run")

try:
	num = int(input("Enter the number"))
	print(type(num))
	if type(num) == 'int':
		raise Exception("ERROR")
except Exception as error:
	print("Please enter your name")

level = 21	
#print(dir(Exceptions))
try:
	if level < 20:
		raise ValueError
      # The code below to this would not be executed
      # if we raise the exception
	    
except ValueError:
	print("I am here")
