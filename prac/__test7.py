x = 1
def f1():
	x = 3
	print(x)
	
f1()
print(x)

import math
print(math.sqrt(25))

print(list("Divine"))

print("welcome to python".split())

print("xyyzxyzxzxyy".count('yy'))

numbers = [1,2,3,4]
numbers.append([5,6,7,8])
print(len(numbers))

values = [[3,4,5,1],[33,6,1,2]]

v = values[0][0]
for lst in values:
	for element in lst:
		if v > element:
			v = element
			
print(v)

print("------------------------------------------------")
mylist = [1,2,3,4,5,6]
for i in range(1,6):
	mylist[i-1] = mylist[i]
	#print(i)
	print(mylist[i])
print("end\n")
	
for i in range(0,6):
	#print(i)		#lat number is not included in the range 
	#print(mylist[i],end="")
	
