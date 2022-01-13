def sum(n1,n2,n3):
    if(n1==n2==n3):
        n4=n1+n2+n3
        n5=n4*3
        print("Sum=",n4)
        print("Thrice of digit:",n5)
    else:
        n4=n1+n2+n3
        print("Sum=",n4)


n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2st number:"))
n3=int(input("Enter 3st number:"))
sum(n1,n2,n3)
