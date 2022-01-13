def neon(n1,n3,sum):
    print("Square of number:",n3)
    print("Sum of square of number:",sum)
    if(n1==sum):
        print("It is a neon number")
    else:
        print("It is not a neon number")


n1=int(input("Enter the number:"))
n2=n1*n1
n3=n2
sum=0
while (n2 != 0):
       sum = (sum + (n2%10))
       n2 = n2//10

neon(n1,n3,sum)       


       
       
