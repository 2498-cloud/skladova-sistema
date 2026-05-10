import json
from models import Product

FILE = "data.json"
products = []

def load_data():
    global products
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            products = [Product.from_dict(p) for p in data]
    except:
        products = []

def save_data():
    with open(FILE, "w") as f:
        json.dump([p.to_dict() for p in products], f, indent=4)

def add_product():
    name = input("Име: ")
    quantity = int(input("Количество: "))
    price = float(input("Цена: "))
    products.append(Product(name, quantity, price))
    save_data()

def show_products():
    if not products:
        print("Няма продукти")
    for p in products:
        print(p)

def find_product():
    name = input("Търси продукт: ")
    for p in products:
        if p.name == name:
            print(p)
            return p
    print("Не е намерен")
    return None

def delete_product():
    name = input("Изтрий продукт: ")
    global products
    products = [p for p in products if p.name != name]
    save_data()

def sell_product():
    p = find_product()
    if p:
        amount = int(input("Количество: "))
        if p.sell(amount):
            print("Продадено")
            save_data()
        else:
            print("Недостатъчно количество")

def menu():
    while True:
        print("\n1. Добави")
        print("2. Покажи")
        print("3. Търси")
        print("4. Продай")
        print("5. Изтрий")
        print("6. Изход")

        choice = input("Избор: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            show_products()
        elif choice == "3":
            find_product()
        elif choice == "4":
            sell_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            break

load_data()
menu()