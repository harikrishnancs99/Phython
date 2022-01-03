for i in range(1,16,1):
    if(i%3==0 and i%5==0):
        print("C")
    elif(i%3==0):
        print("A")
    elif(i%5==0):
        print("B")
    else:
        print(i)
