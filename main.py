qtde = int(input("Digite a quantidade de notas: "))
notas = []
pesos = []
for i in range(qtde):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    peso = float(input("Digite o peso da respectiva nota: "))
    notas.append(nota * peso)
    pesos.append(peso)
    print('\n')

print(f"A média ponderada é: {sum(notas) / sum(pesos):.2f}")