pessoa = {"nome": "guilherme", "idade": 28}

pessoa = dict(nome="guilherme", idade=28)

pessoa["telefone"] = "3333-6631"



contatos = {

    "ana.silva@example.com": {"nome": "Ana Silva", "email": "ana.silva@example.com", "cidade": "São Paulo", "telefone": "(11) 91234-5678"},
    "bruno.souza@example.com": {"nome": "Bruno Souza", "email": "bruno.souza@example.com", "cidade": "Rio de Janeiro", "telefone": "(21) 99876-5432"},
    "carla.pereira@example.com": {"nome": "Carla Pereira", "email": "carla.pereira@example.com", "cidade": "Belo Horizonte", "telefone": "(31) 93456-7890"},
    "diego.costa@example.com": {"nome": "Diego Costa", "email": "diego.costa@example.com", "cidade": "Curitiba", "telefone": "(41) 98765-4321"},
     "elisa.ramos@example.com": {"nome": "Elisa Ramos", "email": "elisa.ramos@example.com", "cidade": "Porto Alegre", "telefone": "(51) 91234-5678"},
    "fernando.lima@example.com": {"nome": "Fernando Lima", "email": "fernando.lima@example.com", "cidade": "Brasília", "telefone": "(61) 97654-3210"},
    "gabriela.azevedo@example.com": {"nome": "Gabriela Azevedo", "email": "gabriela.azevedo@example.com", "cidade": "Salvador", "telefone": "(71) 94567-8901"},
    "henrique.barbosa@example.com": {"nome": "Henrique Barbosa", "email": "henrique.barbosa@example.com", "cidade": "Fortaleza", "telefone": "(85) 98765-4321"},
    "isabela.rocha@example.com": {"nome": "Isabela Rocha", "email": "isabela.rocha@example.com", "cidade": "Recife", "telefone": "(81) 93456-7890"},
    "joao.mendes@example.com": {"nome": "João Mendes", "email": "joao.mendes@example.com", "cidade": "Manaus", "telefone": "(92) 99876-5432"}
}

for chave in contatos:
    
    print(chave, contatos["ana.silva@example.com"]["nome"])
    
for chave, valor in contatos.items():
    print(chave, valor)
