isPalindrome = 0
strSize = 0
text = ""
str = ""
rts = ""

text = input()

str = text.replace(" ", "")

strSize = len(str)
for i in range(strSize, 0, -1):
    rts += str[i-1]

j = 0
for l in str:
    if l == rts[j]:
        isPalindrome += 1
    j += 1

if isPalindrome == strSize:
    print("É palíndromo")
else:
    print("Não é palíndromo")