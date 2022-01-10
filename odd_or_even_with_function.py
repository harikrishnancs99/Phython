def oddeven(n):
    return(n%2)==0

n=int(input("Enter number:"))

if(oddeven(n)):
    print("The number is even")
else:
    print("The number is odd")
