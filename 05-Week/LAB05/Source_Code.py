count = 0

try:
    number = int(input())
except:
    print("Entrada inválida")
else:
    if number < 1 or number > 10:
        print("Entrada inválida")

    else:
        while count < 10:
            count += 1
            result = number * count
            print(number, "x", count, "=", result)