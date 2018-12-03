num=int(input("enter the number:"))
for i in range(1,num+1): #for rows
    for j in range(1,i+1): #for columns
        print("*",end=" ")
    print()
