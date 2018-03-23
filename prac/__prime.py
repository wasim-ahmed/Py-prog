num = int(input("Enter the number:"))
Max_div = int(num / 2)
print("------------Max_dev:",Max_div)
div = int(2)
counter = 1
while div <= Max_div:
	if num % div  == 0:
		break
	else:
		div = div + 1
		counter = counter + 1
		print("before the flood",counter)
		continue
		print("after the flood")
	print("div:/tMax_div",div,Max_div)
	
print("Div out of loop",div)	
div = div - 1
if div == Max_div:
	print("Prime")
else:
	print("Not Prime")
