import copy

#Strings are iteratable like List
Str = "this is a test string"
for c in Str:
	print(c)

#use of in keyword
	
Lx = ["gilfoyle","richard","dinesh","jared","erlich","jing yang"]
print("richard" in Lx)
print("gavin" in Lx)

#another way of initializing a list

X = range(1,10)
for x in X:
	print(x)
	
	
#use of and keyword
age = int(input("Enter age:"))
if age >=10 and age <=20:
	print("you good")
else:
	print("you bad")
	
print("-----------------------------------------------------------------")

#Lx = list("MalayalaM")
#Lx = list("never odd or even")
Lx = list("madam i am adam")
print(Lx)
Lx.reverse()
print(Lx)

#Ly = copy.copy(Lx.reverse())
Ly = copy.copy(Lx)
print(Ly)

Lx.reverse()

print(Lx)

size = len(Lx)
print(size)

div = int(size/2)
print("Div %s" % div)

for i in range(0,div):
	if Lx[i] == Ly[i]:
		print("i = %s" % i)
		#print("Match")
		print(Lx[i])
	else:
		pass

i += 1		
print("i%s" % i)

if i == div:
	print("Matched")
else:
	print("No Match")