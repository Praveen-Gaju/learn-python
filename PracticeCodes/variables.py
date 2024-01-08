"""
Rules for Naming variable
1. start from a-z, A-Z,  and _(underscore)
2. can contain 0-9, a-z, A-Z,  and _(underscore)
3. Case sensitive Abc and ABC is different
4. 33 reserved vaiables in python
"""

a=100
b=50
c=200
d=a+b+c

print(a,b,c)


print("Your answer is",c)
print("Sum of",a,"and",b,"is",c)
#F-String
print(f"sum of {a} and {b} is {c}")
