def pesquisa_populacional():
    dados = []
    
    while True:
        # Coleta de dados do usuário
        sexo = input("Digite o sexo (masculino/feminino) ou 'sair' para finalizar: ").strip().lower()
        if sexo == 'sair':
            break
        
        cor_olhos = input("Digite a cor dos olhos (azuis/verdens/castanhos): ").strip().lower()
        cor_cabelos = input("Digite a cor dos cabelos (louros/castanhos/pretos): ").strip().lower()
        idade = int(input("Digite a idade: "))
        
        dados.append({'sexo': sexo, 'cor_olhos': cor_olhos, 'cor_cabelos': cor_cabelos, 'idade': idade})

    if not dados:
        print("Nenhum dado foi registrado.")
        return

    # a) Calcular maior, menor e média das idades
    idades = [habitante['idade'] for habitante in dados]
    maior_idade = max(idades)
    menor_idade = min(idades)
    media_idade = sum(idades) / len(idades)

    # b) Contar mulheres entre 18 e 35 anos
    mulheres_entre_18_35 = sum(1 for habitante in dados if habitante['sexo'] == 'feminino' and 18 <= habitante['idade'] <= 35)

    # c) Contar indivíduos com olhos verdes e cabelos louros
    individuos_verdes_louros = sum(1 for habitante in dados if habitante['cor_olhos'] == 'verdes' and habitante['cor_cabelos'] == 'louros')

    # Exibir resultados
    print(f"\nMaior Idade: {maior_idade}")
    print(f"Menor Idade: {menor_idade}")
    print(f"Média das Idades: {media_idade:.2f}")
    print(f"Quantidade de mulheres entre 18 e 35 anos: {mulheres_entre_18_35}")
    print(f"Quantidade de indivíduos com olhos verdes e cabelos louros: {individuos_verdes_louros}")

# Executa a função
pesquisa_populacional()