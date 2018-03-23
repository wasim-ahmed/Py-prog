var1 = 0
var2 = 1
num = 0
while num <100:
	num = var1 + var2
	var2 = var1
	var1 = num
	print(num)