import datetime

data_atual = datetime.datetime.now()

# metodo de mascara horas para formatação convencional da região 
print(data_atual.strftime("%d/%b/%Y"))
print(data_atual.strftime("%d/%B/%Y"))
print(data_atual.strftime("%d/%m/%Y"))
print(data_atual.strftime("%H:%M:%S"))



date_string = "20/07/2023 15:30"
data_string_update = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(data_string_update)