#the variables which starts with an underscore are not imported
import sys,copy
print(sys.path)
print(dir(copy))

print(copy.__file__)
print(sys.__package__)
print(copy.__doc__)
print(copy.__dict__)