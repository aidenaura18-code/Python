for i in range(1,4):
    for space in range(3-i):
        print(" ",end=" ")
    for star in range(2*i-1):
        print("*",end=" ")
    print()


num=1
for i in range(1,5):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()