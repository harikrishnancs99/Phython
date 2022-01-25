a=int(input("Enter the side of a square:"))
square=lambda a:(a*a)
x=square(a)
print(x)
l=int(input("Enter the length of a rectangle:"))
b=int(input("Enter the breadth of a rectangle:"))
area2=lambda l,b:l*b
y=area2(l,b)
print(y)
b1=int(input("Enter the base of a triangle:"))
h=int(input("Enter the height of a triangle:"))
area3=lambda b1,h:0.5*b1*h
z=area3(b1,h)
print(z)
