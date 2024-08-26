from datetime import date, datetime, timedelta

data = date.today()

data_time = datetime.today()
print(f"hoje é {data}")
print(f"hoje é {data_time}")

data_upadate = data_time + timedelta(weeks=1)

print(data_upadate)