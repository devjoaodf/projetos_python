itens =[]
for i in range(3):
    item = input()
    itens.append(item)
    i +=1
# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")