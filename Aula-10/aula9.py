numero = 0

while numero <= 1000:
    print(numero)
    numero +=1

nomes = []
contador = 0

while contador < 10:
    nome = input(f"Digite o nome da {contador + 1}ª pessoa: ")
    nomes.append(nome)
    contador += 1

print("\nNomes cadastrados:")
indice = 0
while indice < len(nomes):
    print(nomes[indice])
    indice += 1




  