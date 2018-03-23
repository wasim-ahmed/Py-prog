import keyword

print("a:%s"%"10")
print("b:%s" % 20)
print("c=%s" % (30))
print("%s=%s" % ("x",50))

print("this is {a}".format(a = 10))

x= 100
print(id(x))
print(type(x))
print(keyword.kwlist)


G = 2 + 5j
print(G.real)
print(G.imag)
print(G.conjugate())

N = 12
print(hex(N))
print(oct(N))

print(round(12.3,1))