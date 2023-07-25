#easy challenge
def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False

    return True

def main():
    try:
        num = int(input("Bir sayı girin: "))
        if is_prime(num):
            print(f"{num} bir asal sayıdır.")
        else:
            print(f"{num} bir asal sayı değildir.")
    except ValueError:
        print("Geçerli bir tam sayı girmediniz!")

#medium challenge
if __name__ == "__main__":
    main()

def to_upper_case(text):
    return text.upper()

def main():
    metin = input("Metni girin: ")
    buyuk_metin = to_upper_case(metin)
    print("Büyük harflerle yazılmış hali:", buyuk_metin)

if __name__ == "__main__":
    main()