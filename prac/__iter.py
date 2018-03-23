Dx = {"one":1,"two":2,"three":3}
for i in Dx:
	print(i)
	
def some_function():
    for i in range(4):
        yield i

for i in some_function():
    print(i)
			
