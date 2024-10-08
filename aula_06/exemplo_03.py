nomes = []
medias = []
resp = "S"
while resp == "S" or resp == "s":
     nomes.append(input("informe o nome do estudante: "))
     medias.append(float(input("informe a media do estudante")))
     resp = input("deseja continuar(S/N)? ")
for i in range(len(medias)):
 print(i," -",nomes[i],"- ",medias[i])
maior_media = max(medias)  
pos = medias.index(maior_media)
print(f"{nomes[pos]},voce possui a maior media")
print(f"A media da turma é {(sum(medias)/len(medias)):.1f}")
print(f"A maior media da turma é {max(medias)}")
print(f"A menor media da turma é {min(medias)}")
print(f"A amplitude da media da turma é {max(medias)-min(medias)}")
medias.sort()
daprint(medias)