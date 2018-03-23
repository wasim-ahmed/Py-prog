D = {"numbers":[1,2,3,4,5,6,7,8,9],'alphabets':"abcdefghijklmnopqrstuvwxyz","single_value":13,'always':''}
print(D.keys())
print(D.values())

print(D['numbers'])

print(D.items())

print(D.get('single_value'))

#D.pop('single_value')
D.popitem()
print(D)

D['numbers'] = [10,20,30,40,50,60,70,80,90]
print(D)

Dx = D.copy()
print(Dx)

Dx.clear()
print(Dx)

Dx = D.copy()
del Dx['alphabets']
print(Dx)

Dm = {'first':1,'second':2}
Dn = {'first':100,'third':300}
Dm.update(Dn)	#combining Dictionaries
print(Dm)

	
	