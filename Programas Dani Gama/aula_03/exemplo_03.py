h = float(input("informe a altura: "))
s = input("Informe M - para Masculino d F - para feminino")
if s == "M":
  m = (72.7 * h) - 58
  print(f"O seu peso ideal é (m:.2f)")
elif s == "F" or s == "f":
  f = (62.1 * h) - 44.7
  print(f"o seu peso ideal é {f:.2f})") 
else:
  print("Verifique o sexo informado")







