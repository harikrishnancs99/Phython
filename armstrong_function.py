def arm(n):
    temp=n
    sum=0
    while(n>0):
        r=n%10
        sum=sum+(r*r*r)
        n=n//10
    if(sum==temp):
        print("Armstrong number")
    else:
        print("Not an armstrong number")


n=int(input("Enter a number:"))
arm(n)    
