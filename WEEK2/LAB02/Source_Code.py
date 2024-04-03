distance = float(input())
speed = float(input())

if (distance < 0 or speed < 0):
    print ("Valor inválido!")
    exit()

time = distance / speed

print("O tempo estimado de viagem é", time, "horas.")