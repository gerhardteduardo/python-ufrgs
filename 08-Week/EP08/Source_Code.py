# ** Declarations ** #

# Defines
NUMBERS = "0123456789"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
MAX_SIZE = 20
MIN_SIZE = 6

# Variables
nicePassword = False
checkRepeated = False
checkUpercase = False
checkLowercase = False
checkNumber = False
check = 0
step = 0
i = 0

# ** Main Code ** #

password = input()

while True:
    if step == 0:
        if len(password) >= MIN_SIZE and len(password) <= MAX_SIZE:
            step = 1
        else:
            break

    if step == 1:
        for l in password:
            if (l in UPPERCASE):
                checkUpercase = True
            elif (l in LOWERCASE):
                checkLowercase = True
            elif (l in NUMBERS):
                checkNumber = True
        
        if checkUpercase and checkLowercase and checkNumber:
            step = 2
        else:
            break

    if step == 2:
        for j in password:
            if i < (len(password) - 1):
                if j == password[i+1]:
                    checkRepeated = True
            i += 1

        if checkRepeated != True:
            nicePassword = True
        break

if nicePassword == True:
    print("Senha forte")
else:
    print("Senha fraca")