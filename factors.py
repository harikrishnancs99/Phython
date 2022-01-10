n=int(input("Enter number:"))
if(n<=0):
    print("Cant provide factors")
else:
    for i in range(1,((n//2)+1)):
        if n%i == 0:
            print(i)

print(n)        
