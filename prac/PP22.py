with open('nameslist.txt','r') as Fd:
	text = Fd.read()
	
#print(text)

#print(text.split())
Lx = text.split()
#print(Lx)

Sx = set(Lx)
#print(Sx)
#print(type(Sx))

#for i in Sx:
	#print(i)
	
for i in Sx:
	print("%s is %s times" % (i,Lx.count(i)))
	
print("--------------------------------Extra------------------------------")	
Lx1 = []
with open('Training_01.txt','r') as Fd1:
	line = Fd1.readline()
	while line:
		#print(line)
		words = line.split('/')#splits the line by splitter given by user and returns an array
		#print(words[2])
		Lx1.append(words[2])
		line = Fd1.readline()
		
#print(Lx1)
Sx1 = set(Lx1)
print(Sx1)

for i1 in Sx1:
	print("%s is %s times" % (i1,Lx1.count(i1)))