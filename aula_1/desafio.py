nome= (input("Digite seu nome: "))
salário= float(input("Digite o valor do seu salário: "))
porc_bonus=float(input("Digite o percentual do seu bônus: "))

kpi_bonus=(1000+salário*porc_bonus)

print("Olá "+nome+", o seu valor bônus foi de "+str(kpi_bonus))