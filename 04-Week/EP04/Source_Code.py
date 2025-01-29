try:
    altura = float(input())
    massa = float(input())

except:
    print("Entrada inválida")

else:
    IMC = massa / (altura**2)

    if IMC >= 40:
        print("Obesidade III (mórbida) - IMC: %.1f" % (IMC))

    elif IMC >= 35:
        print("Obesidade II (severa) - IMC: %.1f" % (IMC))

    elif IMC >= 30:
        print("Obesidade I - IMC: %.1f" % (IMC))

    elif IMC >= 25:
        print("Acima do peso - IMC: %.1f" % (IMC))

    elif IMC >= 18.50:
        print("Peso normal - IMC: %.1f" % (IMC))
        
    elif IMC >= 17:
        print("Abaixo do peso - IMC: %.1f" % (IMC))
        
    else:
        print("Muito abaixo do peso - IMC: %.1f" % (IMC))