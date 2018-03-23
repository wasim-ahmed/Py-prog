import sys

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

X1= [i for i in a]	#syntax:new list = [expression, for loop,]
print(X1)

X2 = [i for i in range(10)]
print(X2)

print(sys.argv[0])

X3 = X2 = [i*i for i in range(10)] #[expression - loop - condition]
print(X3)

X4 = [i for i in range(10) if i%2 == 0] #[expression - lopp - condition]
print(X4)

X5 = [i*i for i in a if i%2 == 0] #[expression - lopp - condition]
print(X5)


'''
First For loop is evaluated
then
Condition is evaluated
then
expression is evaluated
'''

str = "this is a digit 12 in this sentence"

X6 = [i for i in str if i.isdigit() == True ] #extracting digit / alphabets in string
print(X6)

Fd = open("RNS_Address.txt","r") #extracting a particular line in file

X7 = [res for res in Fd if "HOMEWOOD" in res]
print(X7)