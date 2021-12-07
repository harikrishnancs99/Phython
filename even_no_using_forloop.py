x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))

if(x>=y):
    print("Not possible")
    exit()
    
if(x%2!=0):
   x+=1
   
for i in range(x,y+1,2):
    print(i)
   
