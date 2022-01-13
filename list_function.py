def common(n_list,n1_list):
    if(n_list==n1_list):
        print("Common")
    else:
        print("Not common")



n_list=[]
n=int(input("Enter Size:"))
for i in range(0, n):
    print("Enter data at index", i )
    item = (input())
    n_list.append(item)
print("First list is ", n_list)

n1_list=[]
o=int(input("Enter Size:"))
for j in range(0, o):
    print("Enter data at index", j )
    item1 =(input())
    n1_list.append(item1)
print("Second list is ", n1_list)

common(n_list,n1_list)
