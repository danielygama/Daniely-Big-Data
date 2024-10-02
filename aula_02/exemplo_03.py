#valor de uma prestação em atraso
# prestacao = float(input("informe o valor da prestacao:  "))
taxa = int(input("informe a taxa de juros mensal: "))
tempo = int(input("Informe a quantidade de meses em atraso: "))
valor_final = prestacao+(prestacao*taxa/100*tempo)
print(f"O valor em atraso sera de R$(valor_final:.2f )")