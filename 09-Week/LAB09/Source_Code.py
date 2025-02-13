# ** Declarations ** #

# Defines
VOWEL = "aeiou"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# Variables
strSize = 0
vowelFreq = 0
consonantFreq = 0

d = {letter: 0 for letter in ALPHABET}

# ** Main Code ** #

phrase = input()
str = phrase.replace(" ", "")
str = str.lower()

for l in str:
    for i in d:
        if l == i:
            d[l] += 1

strSize = sum(d.values())

print ("Letra\tOcorrência\tFrequência")

for j in d:
    if j in str:
        print(f"{j}\t{d[j]}\t\t%.2f" % (d[j]/strSize))

    if j in VOWEL:
        vowelFreq += d[j]
    else:
        consonantFreq += d[j]
        
print(f"Frequência de vogais: %.2f" % (vowelFreq/strSize))
print(f"Frequência de consoantes: %.2f" % (consonantFreq/strSize))