value = int(input())

hours = value // 3600

minutes = value // 60 - ((hours * 60))

seconds = value - (hours * 3600) - (minutes * 60)

print("Este valor corresponde a", hours,"hora(s)", minutes, "minuto(s) e", seconds, "segundo(s).")