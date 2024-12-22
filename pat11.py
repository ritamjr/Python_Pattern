# 15 14 13 12 11
# 10 9 8 7 
# 6 5 4
# 3 2 
# 1

c=15
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(c,end=" ")
        c-=1
    print()
        