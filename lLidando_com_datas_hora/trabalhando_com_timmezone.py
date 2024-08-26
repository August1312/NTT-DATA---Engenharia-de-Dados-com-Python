import datetime, pytz

data_utc = datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")
data_atual = datetime.datetime.now(pytz.timezone("America/Sao_Paulo")).strftime("%d/%m/%Y %H:%M:%S")

print(data_atual)
print(data_utc)

