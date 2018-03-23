try:
	list = [1,2,3,4,5]
	x = list[5]
	print("Success")
except IndexError:
	print("Index out of bound")
else:
	print("All is well")
finally:
	print("I am saved")
	