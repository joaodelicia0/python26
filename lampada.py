watts_metro = 18
largura_metro = float(input("Digite a largura: "))
comprimento_metro = float(input("Digite o comprimento: "))
area = largura_metro * comprimento_metro
watts_necessarios = area * watts_metro
lampada_usada = int(input("Digite a potência da lâmpada: "))
lampadas_necessarias = watts_necessarios / lampada_usada
print(f"Serão necessárias {lampadas_necessarias} lâmpadas.")






