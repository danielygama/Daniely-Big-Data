
vendedores = {
    "Maria": [800, 700, 1000, 900, 1200, 600, 600],
    "João": [900, 500, 1100, 1000, 900, 500, 700],
    "Manuel": [700, 600, 900, 1200, 900, 700, 400]
}

# Inicializando lista para armazenar resultados
resultados = []

# Calculando a média, o maior e o menor valor vendido para cada vendedor
for vendedor, vendas in vendedores.items():
    media_venda = sum(vendas) / len(vendas)
    maior_venda = max(vendas)
    menor_venda = min(vendas)
    
    resultados.append((vendedor, media_venda, maior_venda, menor_venda))

# Exibindo os resultados
print("Resultados de vendas dos últimos 7 dias:")
print("{:<10} | {:<10} | {:<10} | {:<10}".format("Vendedor", "Média", "Maior", "Menor"))
print("-" * 50)

for resultado in resultados:
    vendedor, media, maior, menor = resultado
    print("{:<10} | {:<10.2f} | {:<10} | {:<10}".format(vendedor, media, maior, menor))