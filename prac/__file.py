#File read
Fd = open("Account_Number.txt",'r')
while True:
	if len(Fd.readline()) ==  0:
		break
	print(Fd.readline())

Fd.close()

Fx = open("Account_Number.txt",'r')
for line in Fx.readlines():
	print(line)

Fx.close()
print(Fx.closed)

#File write

F = open("__test.txt",'w')
F.write("this is first line")
print(F.tell(4)) #argument is required
F.seek()
print("----->------------>----------->",F.tell())
F.write(" ******* ")

#print(dir(__builtins__))