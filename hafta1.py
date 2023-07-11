from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year

    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1

    return age

birth_date_str = input("Doğum tarihinizi (GG/AA/YYYY formatında) girin: ")

birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")

age = calculate_age(birth_date)


print("Yaşınız :", age)
