MAX_VALUE = 100
MIN_VALUE = 0
AVARAGE_VALUE = 75

Nota = float(input())
Freq = float(input())

if Nota < MIN_VALUE or Nota > MAX_VALUE:
    print("Entrada inválida")
    exit()

if Freq < MIN_VALUE or Freq > MAX_VALUE:
    print("Entrada inválida")
    exit()

if Freq < AVARAGE_VALUE:
    print("Reprovado")
elif Nota >= AVARAGE_VALUE:
    print("Aprovado")
else:
    print("Exame")