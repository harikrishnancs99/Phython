n=int(input("Enter a number:"))
o=int(input("Enter 2nd number:"))
f=0
for i in range(n,o+1):
    f=0
    for j in range(2, ((i//2)+1)):
        if(i%j==0):
            f=f+1
            break
    if f==0 and i!=1:
        print(i)
