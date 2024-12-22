# 5 5 5 5 5 
# 5 4 4 4 4
# 5 4 3 3 3
# 5 4 3 2 2
# 5 4 3 2 1

for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    for k in range (1,i):
        print(i,end=" ")
    print()
