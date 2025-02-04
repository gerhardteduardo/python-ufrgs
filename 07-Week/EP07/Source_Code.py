# ** Imports ** #

import random

# ** Declarations ** #

# Defines
MAX_NUMBERS = 5

# Variables
run = True
end = False
prizeDraw = False
getPlayersNumbers = True
totalPointsP1 = 0
totalPointsP2 = 0
randomNumber = 0
pointsP1 = 0
pointsP2 = 0

# List
P1 = []
P2 = []
luckNumbers = []

# ** Main Code ** #

while run:
    random.seed(1024)
    while getPlayersNumbers:
        number = int(input())
        if number == 0 and len(P1) == 0:
            getPlayersNumbers = False
            prizeDraw = False
            end = False
            run = False
           
        if number >= 1 and number <= 20:
            if len(P1) < MAX_NUMBERS:
                P1.append(number)
            elif len(P2) < MAX_NUMBERS:
                P2.append(number)

        if len(P1) == MAX_NUMBERS and len(P2) == MAX_NUMBERS:
            getPlayersNumbers = False
            prizeDraw = True

    while prizeDraw:
        if len(luckNumbers) != MAX_NUMBERS:
            randomNumber = random.randint(1, 20)
            if (randomNumber in luckNumbers) == 0:
                luckNumbers.append(randomNumber)
        else:
            for i in range(len(luckNumbers)):
                for j in range(MAX_NUMBERS):
                    if luckNumbers[i] == P1[j]:
                        pointsP1 += 10
                    if luckNumbers[i] == P2[j]:
                        pointsP2 += 10
            prizeDraw = False
            end = True

    if end == True:
        totalPointsP1 += pointsP1
        totalPointsP2 += pointsP2
        print(f"JOGADOR 1 = {pointsP1}, JOGADOR 2 = {pointsP2}")
        P1.clear()
        P2.clear()
        pointsP1 = 0
        pointsP2 = 0
        luckNumbers.clear()
        getPlayersNumbers = True
        prizeDraw = False
        end == False
       
if totalPointsP1 == totalPointsP2:
    print("EMPATE!")
elif totalPointsP1 > totalPointsP2:
    print("JOGADOR 1 VENCEU!")
else:
    print("JOGADOR 2 VENCEU!")