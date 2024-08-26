numeros = set([1, 2, 3, 1, 3, 4])

frutas = set("abacaxi")

carro = set(("palio", "gol", "celta", "palio"))

print(numeros)
print(frutas)
print(carro)

for indece, carro in enumerate(carro):
    print(f"{indece}: {carro}")
    
    
conjunto_a = {1, 2, 4, 5, 66, 677}
conjunto_b = { 55, 56, 89, 86, 34, 432}

teste1 = conjunto_a.union(conjunto_b)
teste2 = conjunto_a.intersection(conjunto_b)
teste4 = conjunto_a.difference(conjunto_b)
teste5 = conjunto_a.difference_update(conjunto_b)

print(f"union: {teste1}")
print(f"intersection: {teste2}")
print(f"diferrence: {teste4}" )
print(f"diference_update: {teste5}")