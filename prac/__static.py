import __fib
def fun():
	fun.var = 10
	fun.var = fun.var + 2
	return fun.var
	
print("------Start-------")
for i in range(5):
	ret = fun()
	print(ret)