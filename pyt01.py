print("Hello ---- world")

name = "Привет"
print(name)
print(type(name))

d = open("/home/smv/python-jms/ooo pyt", "r")
f = d.read()
print(f)

d = open("/home/smv/python-jms/ooo pyt", "r")
f = d.read(2)
print(f)

d = open("/home/smv/python-jms/ooo pyt", "r")
f = d.readlines()
print(f)

d = open("/home/smv/python-jms/ooo pyt", "r")
f = d.readline()
print(f)
d.close()