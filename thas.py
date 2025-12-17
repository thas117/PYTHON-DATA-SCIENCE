a = 89
b = 73
c = 90
average = (a +b+c/4)
print(average)
total = a+b+c
print(total)
subtract = (a-b)
divide = (c/b)
print(subtract)
print(divide)

# in, not in
'a' in 'apple'
'a' not in 'apple'
# is, is not
'x' is 'y'
'x' is not 'y'

a=10
b=20
print(a&b)
print(a|b)
print(a^b)
print(a!=b)
print (a==b)

i=30
j=30
if i<j:
    print("i is lesser than j")
elif i>j:
    print("i is greater than j")
else:
    print("Both are equal")


a=50
if a<50:
    print("fail")
elif a>50:
    print("pass")
else:
    print("a is equal to 50")

a=17
b=1
a=b

a="@" 
b=2*a
print(b)

mark=50
a="pass" if mark>30 else"fail"
print(a)

num=int(input("Enter a number:"))
if num>0:
    print(num,"is positive")
elif num<0:
    print(num,"is negative")
else:
    print(num,"is equal to 0")

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
if a>b and a>c:
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
else:
    print("c is greatest")

for i in range(3,15,3):
    print("thas")

