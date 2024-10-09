def temperaturas():
    temperaturas = []
    
    while True:
        entrada = input("Digite uma temperatura (ou 'sair' para finalizar): ")
        
        if entrada.lower() == 'sair':
            break
        
        try:
            temperatura = float(entrada)
            temperaturas.append(temperatura)
        except ValueError:
            print("Por favor, digite um número válido.")

    if temperaturas:
        menor_temp = min(temperaturas)
        maior_temp = max(temperaturas)
        media_temp = sum(temperaturas) / len(temperaturas)

        print(f"\nMenor Temperatura: {menor_temp:.2f}°C")
        print(f"Maior Temperatura: {maior_temp:.2f}°C")
        print(f"Média das Temperaturas: {media_temp:.2f}°C")
    else:
        print("Nenhuma temperatura foi registrada.")

# Executa a função
temperaturas()


