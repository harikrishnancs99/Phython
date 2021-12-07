x=int(input("Enter a number:"))
f=0
s=1
if(x<0):
      print("Count is zero")
      exit()
      
if(x>=1):
      print(f)

if(x>=2):
      print(s)
      for i in range(1, x-1):
          print(f+s)
          t=f
          f=s
          s=t+s
      
