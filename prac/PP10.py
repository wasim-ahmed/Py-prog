a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

X = [i for i in a if i in b] # this will print the common in both the list but misses if there is repeat in first list

print(X)

Y = [i for i in set(a) if i in b]
print(Y)

Sample = [1,5,2,78,5,5,3,89,78]
print(Sample)
print(set(Sample)) #set sorts and give the unique elements