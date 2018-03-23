import string,random

#print(string.ascii_letters)
#print(string.digits)
#print(string.punctuation)

Mask = string.ascii_letters + string.digits + string.punctuation

#print(Mask)
len = 8
X = "".join(random.sample(Mask,len)) #generates random output from given list of given length

print(X)