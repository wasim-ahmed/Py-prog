import copy
import bisect
mylist = [1,2,3,4,5,"cat","dog",12.4] #a hetrogeneous mixtures
size = len(mylist)
for i in range(len(mylist)):
	print(mylist[i])
	
print(mylist)
mylist.append('django')
print(mylist)
#mylist.append(['this', 'is', 'a', 'new', 'list'])#new list appended
#print(mylist)
#print(len(mylist))#considered the appended list as 1 item

mylist.extend(['this', 'is', 'a', 'new', 'list'])#new list extended, considered as part of list
print(mylist)
print(len(mylist))

mylist.append('this')

print("The index of this:",mylist.index('this'))# and index starts from 0, gives only the first occurance

mylist.insert(8,'insertion')# 8th position starting from 0
print(mylist)

mylist.remove('django')
print(mylist)

#mylist.pop()
#print(mylist)

print(mylist.count('this'))

#mylist.sort() #can sort only 1 type of data
print(mylist)

mylist.reverse()
print(mylist)

print("------------------------------------------------------------------------")

L1 = [1,2,3]
L1 += [4]
L2 = ['a','b','c']
L3 = L1 + L2
print(L3)

L3 *= 2
print(L3) # replicates the element

print("--------------------------------------------------------------------------------------")

Lz = [10,20,30,40,50,60,70,80,90,100] #index starts from 1 
print(Lz[::])
print(Lz[0::])
print(Lz[1::])
print(Lz[:0:])
print(Lz[:1:])
print(Lz[:2:])
print(Lz[1::2])
print(Lz[:6:2])

print("--------------------------------------------------------------------------------------")

Lx = [10,20,30,40,50]
#Ly = Lx # this is not a copy it creates a reference 
Ly = copy.copy(Lx) # Shalloow copy
print(Ly)

Lx[2] = 73
print(Lx)
print(Ly) 

La = [10,20,30,[11,22]]
Lb = copy.deepcopy(La) # deep copy
La[3][0] = 99
print(La)
print(Lb)

print("--------------------------------------------------------------------------------------")

Lm = [13,7,89,56,103,34]
Lm.sort()
bisect.insort(Lm,23)#insert it at required location as if sorted
print(Lm)
print(bisect.bisect(Lm,67))
