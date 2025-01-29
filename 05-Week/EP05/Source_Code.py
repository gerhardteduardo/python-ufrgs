old = "Não"
count = 0
min_years = 1000
max_salary = 0
total_salary = 0
run = "S"

while run == "S":
    count += 1
    name = input()
    years = int(input())
    salary = float(input())
    run = input()

    if salary >= max_salary:
        rich_name = name
        max_salary = salary
    
    total_salary = salary + total_salary
    average_salary = total_salary / count

    if years <= min_years:
        min_years = years

    if years >= 65:
        old = "Sim"

print("- Relatório da Pesquisa -")
print("Menor idade:", min_years)
print(f"Salário médio: R$ %.2f" % average_salary)
print("Nome maior salário:", rich_name)
print("Existe participante idoso:", old)