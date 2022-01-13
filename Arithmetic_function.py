def arithmetic(n1,n2):
    return(n1+n2,n1-n2,n1*n2,n1/n2)
   

num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))

ar_list=arithmetic(num1,num2)
print(f"sum={ar_list[0]}")
print(f"sum={ar_list[1]}")
print(f"sum={ar_list[2]}")
print(f"sum={ar_list[3]}")
