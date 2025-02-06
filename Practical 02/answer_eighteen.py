rows = 3
cols = 7

for i in range(rows):
    for j in range(cols):
        if j == cols // 2 - i or j == cols // 2 + i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("* " + "- " * (cols - 2) + "*")
