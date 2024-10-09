def calcular_salario():
    # Entrada de dados
    valor_hora = float(input("Digite o valor que o funcionário recebe por hora: R$ "))
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

    # Cálculo do salário bruto
    salario_bruto = valor_hora * horas_trabalhadas

    # Cálculo dos descontos
    irrf = salario_bruto * 0.11  # 11% de Imposto de Renda
    inss = salario_bruto * 0.08   # 8% de INSS
    sindicato = salario_bruto * 0.05  # 5% para o sindicato

    # Salário líquido
    salario_liquido = salario_bruto - (irrf + inss + sindicato)

    # Exibição dos resultados
    print("\nResumo do Salário:")
    print(f"Salário Bruto: R$ {salario_bruto:.2f}")
    print(f"Desconto do Imposto de Renda (IRRF - 11%): R$ {irrf:.2f}")
    print(f"Desconto do INSS (8%): R$ {inss:.2f}")
    print(f"Desconto do Sindicato (5%): R$ {sindicato:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

# Executa a função
calcular_salario()