nota = float(input())

if nota < 0 or nota > 100:
    print("Nota inválida")

elif nota >= 90:
    print("Conceito: A")

elif nota >= 80:
    print("Conceito: B")

elif nota >= 70:
    print("Conceito: C")

elif nota >= 60:
    print("Conceito: D")

else:
    print("Conceito: F")