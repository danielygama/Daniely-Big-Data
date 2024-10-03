# Programa média
Nome = input("informe o nome do estudante: ")
n1 = float(input("informe a primeira nota de 0 a 100: "))
n2 = float(input("informe a segunda nota de 0 a 100: "))
media = (n1 + n2) / 2
if media >= 70: 
  print(f"{nome}, você esta Aprovado, pois sua media foi {media:.2f})")
elif media >= 30 and media < 70:
    print(f"{nome}, você esta em Recuperação, pois sua média foi {media:.2f}")
else:
    print("f{}")    
