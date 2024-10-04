try:
   n1 = int(input("informe o primeiro valor: "))
   n2 = int(input("informe o segunda valor: "))
except ValueError:
  print("Verifique a entrada de dados.")
else:
  try:
   result = n1 / n2
  except ZeroDivisionError:  
    print("Não é possivel dividir por zero.")
  else:
   print(result)