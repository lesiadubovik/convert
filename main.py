import requests
from decimal import Decimal
from convert import convert

def main():
    amount = str(input("Введите количество валюты: "))
    from_ = str(input("""Введите ISO-код вашей валюты 
                    (К примеру: RUR-рубль EUR-евро USD-доллар): """))
    to_ = str(input("Введите ISO-код валюты, в которую хотите первести: "))
    date = str(input("Введите дату (пример: 17/02/2005): "))
    result = convert(Decimal(amount), from_, to_, date, requests)
    return result

if __name__ == "__main__":
    print(main())
