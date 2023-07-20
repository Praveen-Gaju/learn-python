#
a = 10
b = 20
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)

#
a = 10
b = 20
c = 30
a, b, c = b, c, a
print(a, b, c)

#
a = 10
b = 20
temp = a
a = b
b = temp
print(a, b)
