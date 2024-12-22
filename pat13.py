# 1
# 3 5
# 7 9 11
# 13 15 17 19
# 21 23 25 27 29

c=1
for i in range(1,6):
    for j in range(1,i+1):
        print(c,end=" ")
        c=c+2
    print()