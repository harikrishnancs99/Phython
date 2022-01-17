a=[1,2,3,4,5]
b=[5,7,8,9,0]
sum1=sum2=0
if len(a)==len(b):
    print("The two lists are equal")
elif len(a)>len(b):
    print("Length of first list is greater")
elif len(b)>len(a):
    print("Length of second list is greater")

for i in a:
    sum1+=i
    
print("The first list sum is:",sum1)
for j in b:
    sum2+=j

print("The second list sum is:",sum2)

if(sum1==sum2):
    print("Sums are equal")
else:
    print("Sums are not equal")

for i in a:
    for j in b:
        if i==j:
            print(j,"is common in both list")
