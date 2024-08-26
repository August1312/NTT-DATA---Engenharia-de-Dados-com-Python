frutas = ["laranja", "maca", "uva"]

frutas = []

letras = list("python")

numeros = list(range(10))

carro = ["ferrari", "f8", 420000, 2020, 2900, "são paulo", True]


matriz = [[1, "a", 2],
          ["b", 3, 4],
          [6, 5, "c"]
          ]

print(matriz[0])
print(matriz[0][0])
print(matriz[-1][-1])


teste =  [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]
print(teste)