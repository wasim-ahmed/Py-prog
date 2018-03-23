import json


info = dict()
with open("sample.json",'r') as Fd:
	info = json.load(Fd)
	
#print(info)

for key,value in info.items():
	#print(key)
	print(value)