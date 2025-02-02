n1_math = 0
n2_math = 0

N1 = int(input())
N2 = int(input())

if N1 > 0 and N2 > 0:

    print(f"Divisores próprios de {N1}: ", end="")
    for i in range(1, N1):
        is_friend = N1 % i

        if is_friend == 0:
            print(f"{i} ", end="")
            n1_math += i

    print(f"cuja soma é {n1_math}")

    print(f"Divisores próprios de {N2}: ", end="")
    for i in range(1, N2):
        is_friend = N2 % i

        if is_friend == 0:
            print(f"{i} ", end="")
            n2_math += i

    print(f"cuja soma é {n2_math}")

    if n1_math == N2 and n2_math == N1:
        print(f"{N1} e {N2} são amigos")
    else:
        print(f"{N1} e {N2} não são amigos")