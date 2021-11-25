x1=int(input("Enter the mark of subject1:"))
x2=int(input("Enter the mark of subject2:"))
x3=int(input("Enter the mark of subject3:"))
x4=int(input("Enter the mark of subject4:"))
x5=int(input("Enter the mark of subject5:"))

total = x1+x2+x3+x4+x5
print(f"Total mark is {total}\n")
average = total/5
print(f"Average is {average}\n")

if average>80:
    print("A grade")
elif average>70:
    print("B grade")
elif average>60:
    print("C grade")
elif average>50:
    print("D grade")
elif average>40:
    print("E grade")
else:
    print("Failed")    
