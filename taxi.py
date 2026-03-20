combustivel = 1.19
inicio_odometro = float(input("Digite qual os quilômetros iniciais do odômetro: "))
fim_odometro = float(input("Digite quais os quilômetros andados no odômetro no final do dia: "))
distancia_andadas = fim_odometro - inicio_odometro
quantidade_combustivel = int(input("Digite a quantidade de litros de combustível colocados no carro: "))
consumo_dia = distancia_andadas / quantidade_combustivel
custo_dia = quantidade_combustivel * combustivel
dinheiro_ganho = float(input("Digite o dinheiro ganho no dia: "))
lucro_dia = dinheiro_ganho - custo_dia
print(f"O consumo do dia foi de: {consumo_dia} quilômetros por litro")
print(f"O lucro do dia foi de: R${lucro_dia}")

