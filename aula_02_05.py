# Dados fornecidos
roubos = [100, 90, 80, 120, 110, 90, 70]
furtos = [80, 60, 70, 60, 100, 50, 30]
recuperacoes = [70, 50, 90, 80, 100, 70, 50]

# Inicializando listas para armazenar resultados
quantidade_diaria = []
taxa_recuperacao_diaria = []

# Calculando a quantidade de roubos + furtos e a taxa de recuperação
for dia in range(7):
    total_roubos_furtos = roubos[dia] + furtos[dia]
    quantidade_diaria.append(total_roubos_furtos)
    
    if roubos[dia] > 0:
        taxa_recuperacao = recuperacoes[dia] / roubos[dia]
    else:
        taxa_recuperacao = 0  # Prevenindo divisão por zero

    taxa_recuperacao_diaria.append(taxa_recuperacao)

# Exibindo os resultados
print("Quantidade de roubos + furtos diários (últimos 7 dias):")
for dia, total in enumerate(quantidade_diaria):
    print(f"Dia {dia + 1}: {total}")

print("\nTaxa de recuperação de automóveis diária (últimos 7 dias):")
for dia, taxa in enumerate(taxa_recuperacao_diaria):
    print(f"Dia {dia + 1}: {taxa:.2%}")  # Formatando como porcentagem