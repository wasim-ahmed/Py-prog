import sys
str = """ This is a sample string """
print(str[6])
print(str[-5])
print(str[2:])

#str[0] = "X" # Strings are immutable

print("The answer is :{a} {b}".format(a = 5,b = 12))

print(str + str)
print(str * 3)

Sx = """ This is a sample string , not now"""
print(str == Sx)

print("-------------------------------------------------------------------")

#Method to Query information 
S1 = "45"
print(S1.isdigit())
S2 = "Hello"
print(S2.isalpha())
S3 = "Hello123"
print(S3.isalnum())
S4 = "UPPER"
print(S4.isupper())
S5 = "lower"
print(S5.islower())
S6 = "Camel"
print(S6.istitle())
S7 = "                   "
print(S7.isspace())

print(str.count('i')) 
print(len(str))

S8 = "this i a test"
print(S8.title())

S9 = "this is in small case"
print(S9.capitalize())

S10 = "this is just a test"
print(S10.upper())

S11 =  "THIS IS JUST A TEST"
print(S11.lower())

S12 = "I Am Just Swapping The Case"
print(S12.swapcase()) 

S13 = "Lets adjust this string"
print(S13.center(40))
print(S13.ljust(20,'-'))
print(S13.rjust(20,'-'))
print(S13.zfill(20))

S14 = "     there are some spaces to left and some spaces to right    "
print(S14.strip())
print(S14.lstrip())
print(S14.rstrip())

S15 = "look\there"
print(S15.expandtabs())

S16 = "this is a dummy string"
print(S16.replace('dummy','great',1))

print(S16.translate('aeiou'))

S17 = "Lets see how partition works"
print(S17.partition('how'))

S18 = "Lets see how split works"
print(S18.split(' ')) # while split the argument is consumed
print(S18.rsplit(' ',2))

S19 = "this is the \n good way to \n split lines"
print(S19.splitlines())

print(sys.getdefaultencoding())


S20  = "this is the final function"
print(S20.startswith('this'))
print(S20.find('is'))
print(S20.endswith('ion'))
print(S20.index('is'))