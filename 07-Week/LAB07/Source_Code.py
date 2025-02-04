# ** Declarations ** #

# Variables
temp_avarage = 0
temp_total = 0
mouth_max = 12
temp = 0

# List
tempList = []
mouthList = []

# ** Main Code ** #

for n in range(0, mouth_max):
    # Get user value
    mouthList.append(input())
    temp = float(input())
    tempList.append(temp)
    # Math
    temp_total += temp
    temp_avarage = round(temp_total/mouth_max, 2)

# Do prints
print("%.2f" % temp_avarage)
for i in range(len(mouthList)):
    if tempList[i] >= temp_avarage:
        print(f"{mouthList[i]} %.2f" % (tempList[i]))
