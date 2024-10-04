try:
    idade = int(input("Informe a sua idade: "))
    tempo_de_trabalho = int(input("Informar o tempo trabalhado: "))
except ValueError:
    print("Verifique os dados informados")
else:    
   if idade >= 65:
    print("Apto a Aposentadoria")
elif tempo_de_trabalho <= 30:
    print("Apto a Aposentadoria")  
elif idade <= 60 and tempo >= 25:
   print("Apto a aposentadoria" 
else:
  print("Inapto a aposentadoria")

