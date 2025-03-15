# Solicita um número ao usuário
numero = int(input("Digite um número para ver sua tabuada: "))
# Gera a tabuada do número de 1 a 10
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero *i}")