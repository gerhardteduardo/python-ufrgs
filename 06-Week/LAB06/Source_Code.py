end = False
L = int(input())
H = int(input())

if L >= 1 and H >= 1:
    for i in range(H):
        if i == 0:
            for j in range(L):
                print("*", end="")
            print()
            
        elif i > 0 and i < (H - 1):
            print("*", end="")
            for j in range(2, L):
                print(" ", end="")

            if L >= 2:
                print("*", end="")
            print()
            
        elif i >= (H - 1):
            for j in range(L):
                print("*", end="")
            print()