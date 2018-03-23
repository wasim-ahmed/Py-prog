Tu = (1,2,3)
print(Tu)
print(Tu[1:]) 
print(Tu[1]) 

#Tu[0] = 7 # immutable 

Tx = 10,20,30,40,50,10
print(Tx)

Ty = (11)
print(Ty)

Tz  = Tx + Tu 
print(Tz)

print(Tx.count(10))
print(Tx.index(30))

#print("Used in dictionaries")

x,y,z = (12,13,14) #assigning value 
print(x)
a,b,c = range(3)
print(a)

#Tuple unpacking

Tm = (89,79,69,59)
a,b,c,d = Tm
print(b)

empty = Tm # copy to an empty tuple
print(empty)

X = 1,2,3
Y = 10,20,30
X = Y # Swapping
print(X)

print(len(X))
print(max(Y))


C = (1,2,3,[10,20,30]) #if the value within a tuple is mutable then only they can be changed
C[3][2] = 22
print(C)
C = (32,33) 
print(C) # but their entire value can be replaced