# Dados fornecidos
populacao_vacinada = [30000000, 25000000, 10000000, 5000000]
populacao_total = [213317639, 214477744, 215574303, 216687971]

# Cálculos
total_vacinados = sum(populacao_vacinada)
media_vacinados = total_vacinados / len(populacao_vacinada)

total_populacao = sum(populacao_total)
media_populacao = total_populacao / len(populacao_total)

taxas_vacinacao = [(vacinados / total) * 100 for vacinados, total in zip(populacao_vacinada, populacao_total)]

# Resultados
print(f"Total de pessoas vacinadas: {total_vacinados}")
print(f"Média de pessoas vacinadas: {media_vacinados:.2f}")
print(f"Total da população: {total_populacao}")
print(f"Média da população: {media_populacao:.2f}")

print("Taxa de vacinação anual:")
for ano, taxa in enumerate(taxas_vacinacao, start=1):
    print(f"Ano {ano}: {taxa:.2f}%")

