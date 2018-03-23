with open("primenumbers.txt",'r') as Fd1:
	file1Content = Fd1.read()
	#print("prime numbers:\n",file1Content)
	
with open("happynumbers.txt",'r') as Fd2:
	file2Content = Fd2.read()
	#print("happy numbers:\n",file2Content)
	
Lx1 = list(file1Content.split())
#print(Lx1)
Lx2 = list(file2Content.split())
#print(Lx2)
'''
for (i,j) in zip(Lx1,Lx2):
	if i == j:
		print(i,j)
'''

Sx1 = set(Lx1)
Sx2 = set(Lx2)
print(Sx1 & Sx2)