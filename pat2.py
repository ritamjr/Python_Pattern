x = 5
for i in range(1, 8, 2):
        print(" " * x, end="")
        x=x-1
        for j in range(1, i + 1):
            if j % 2 == 1:
                print("1", end="")
            else:
                print("*", end="")
        print()

x =x+2
for i in range(5, 0, -2):
        print(" " * x, end="")
        x += 1
        for j in range(1, i + 1):
            if j % 2 == 1:
                print("1", end="")
            else:
                print("*", end="")
        print()
        

