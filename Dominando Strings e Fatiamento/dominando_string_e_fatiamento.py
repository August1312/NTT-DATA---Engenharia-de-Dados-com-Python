curso = ' pYthon '

#metodos python 

print(curso.upper()) #tudo maiuscula 

print(curso.lower())#tudo minuscula 

print(curso.title())#primeira letra maiuscula 

print(curso.strip()) #remove todos os espaços em branco da esqueda e da direita

print(curso.lstrip())#remove o espaço em branco da esqueda 

print(curso.rstrip())# remove o espaço da direita

print(curso.center(10, '#')) #centraliza e modifica a string com caracteres que vc quera coloca no espaço

print('.'.join(curso))# junta caracteres a string com join 

for i in curso:
    print(i, end='-')
print()

print(curso[::-1])