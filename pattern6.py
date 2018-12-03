num=int(input("enter row:"))
for i in range(0,num-1):
    for j in range(0,num-i-1): #to print space
        print("*",end=" ")
    for j in range(0,i+1):
        print(end=" ")  #to print star
    print()
for i in range(num,0,-1):
    for j in range(0,num-i):
        print("*",end=" ")
    for j in range(0,i):
        print(end=" ")
    print()
