n=int(input("Enter number:"))
r=0
b=n
while(n!=0):
    ld=n%10
    r=(r*10)+ld
    n=n//10

if(r==b):
   print("It is palindrome")
else:
   print("It is not palindrome")
