try:
  nome = input("Digite o nome do produto: ")
  Qtd = int(input("Digite a quantidade comprada: "))
  valor = float(input("Digite o preço unitário: "))
except ValueError:
   print("Verifique os valores informados")
else:
  total = valor * Qtd
print(f"O valor total sem desconto é R$ {total:.2f}")
if qtd <= 5:
    desc = total * 0.98
elif Qtd > 5 and Qtd <= 10:
    Desc = total * 0.97
else: 
    desc = total * 0.05
print(f"O valor total com desconto é R$ {desc:.2f}")       

