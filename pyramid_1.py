rows=5
spaces=2*rows-2
for i in range(0,rows):
    for j in range(0,spaces):
        print(end=" ")
    
    spaces=spaces-2

    for j in range(0,i+1):
        print("*",end=" ")

    print("\n")