# ** Declarations ** #

# Variables

d = {}

# ** Main Code ** #

while True:
    app = input()

    if app != "":
        hours = int(input())
        if app in d:
            d[app] += hours
        else:
            d[app] = hours
    else:
        break
      
print ("Aplicativo\tTempo de Utilização")

for i in sorted(d, key = d.get, reverse = True):
    print(f"{i}\t{d[i]}")