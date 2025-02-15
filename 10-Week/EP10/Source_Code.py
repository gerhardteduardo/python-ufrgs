# ** Declarations ** #

m = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
    "agosto", "setembro", "outubro", "novembro", "dezembro"]

d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# ** Definitions ** #

def check_day(D, M):
    x = d[M-1]
    if D <= x :
        return True
    return False

def check_date(D, M, Y):
    if Y > 0 :
        if M >= 1 and M <= 12 :
            if D >= 1 and D <= 31 :
                    return check_day(D, M)
   
    return False
   
# ** Main Code ** #

D, M, Y = input().split("/")

D = int(D)
M = int(M)
Y = int(Y)

if check_date(D, M, Y) == True :
    print(f"{D} de %s de {Y}" % (m[M-1]))
else :
    print("Data inválida")