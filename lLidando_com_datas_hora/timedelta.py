from datetime import timedelta, datetime, time

tipo_carro = input("digite o tamanho do carro: ").upper()  # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"o carro chegou: {data_atual} e ficara pronto as {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"o carro chegou: {data_atual} e ficara pronto as {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"o carro chegou: {data_atual} e ficara pronto as {data_estimada}")

#exibindo somente a hora 
resultado = datetime.now() - timedelta(hours=1)
print(resultado.time())

#exibindo somente data
print(datetime.now().date())