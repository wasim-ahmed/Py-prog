MY_GLOBAL = 45

def fun1():
	global MY_GLOBAL
	MY_GLOBAL = 32
	print(MY_GLOBAL)
	print(globals())
	
def fun2():
	print(MY_GLOBAL)
	
print("-----------Start----------")
fun1()
fun2()