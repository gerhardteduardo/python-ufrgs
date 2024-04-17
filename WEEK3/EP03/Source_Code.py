a = float(input())
b = float(input())
c = float(input())

if a != 0 and b != 0 and c != 0:
    if a <= (b + c) and b <= (a + c) and c <= (a + b):
        
        if a == b == c:
            print("triângulo equilátero")
        elif a != b != c != a:
            print("triângulo escaleno")
        else:
            print("triângulo isósceles")
    else:
        print("triângulo inválido")
else:
    print("triângulo inválido")