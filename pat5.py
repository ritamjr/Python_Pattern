x = 3
y = 0
for i in range(1, 4):
        print(" " * x, end="")
        x -= 1
        for j in range(1, i + 1):
            print(j, end="")
        for a in range(y, 0,-1):
            print(a, end="")
        y += 1
        print()