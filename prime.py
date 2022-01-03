n=int(input("Enter a number:"))
for i in range(2, ((n//2)+1)):
    if(n%i==0):
        print("It is not a prime number")
        exit()

print(f"{n} is a prime number")        

        
