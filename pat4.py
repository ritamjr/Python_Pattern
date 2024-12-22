x = 3
for i in range(1, 4):
        print(" " * (x - i), end="")
        for j in range(i, 0, -1):
            print(j, end="")
        for j in range(2, i + 1):
            print(j, end="")
        print()
