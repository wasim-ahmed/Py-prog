import json


Bx = dict()
Bx = {
	"one":10,
	"two":20
	}

myObj = dict()
myObj = {
	"name":"John",
	"age":30,
	"cars": [
	{"name":"Ford", "models":[ "Fiesta", "Focus", "Mustang"]},
	{"name":"BMW", "models":[ "320", "X3", "X5"]},
	{"name":"Fiat", "models":[ "500", "Panda"]}
	]
	} 

#print(Bx)
print(myObj)

'''
with open("info.json",'w') as Fd:
	json.dump(Bx,Fd)
'''

with open('sample.json','w') as Fd:
	json.dump(myObj,Fd)