from collections import Counter
import csv


def analyze_log(path_to_file):
    if path_to_file.endswith(".csv"):
        try:
            orders = ""
            with open(path_to_file, "r") as file:
                keys = ["name", "order", "weekday"]
                *orders, = csv.DictReader(file, fieldnames=keys)
            
            res1 = most_ordered(orders, 'Maria')[0][0]
            res2 = most_ordered_qty(orders, 'arnaldo', 'hamburguer')
            res3 = never_ordered(orders, 'joao')
            res4 = never_go(orders, 'joao')

            with open("data/mkt_campaign.txt", "w") as file:
                file.write(f"{res1}\n{res2}\n{res3}\n{res4}")

        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
    else:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")


def most_ordered(orders, name):
    items = []
    for order in orders:
        if order["name"] == name.lower():
            items.append(order["order"])
    result = Counter(items).most_common()
    return result


def most_ordered_qty(orders, name, product):
    items = most_ordered(orders, name)
    for item in items:
        if item[0] == product.lower():
            return item[1]


def never_ordered(orders, name):
    personal = most_ordered(orders, name)
    personal_set = [item[0] for item in personal]
    orders_order = []
    for order in orders:
        orders_order.append(order["order"])
    total = Counter(orders_order).most_common()
    total_set = [item[0] for item in total]
    return set(total_set) - set(personal_set)


def never_go(orders, name):
    personal_weekday = [order["weekday"] for order in orders if order["name"] == name.lower()]
    personal = Counter(personal_weekday).most_common()
    personal_set = [item[0] for item in personal]
    orders_order = [order["weekday"] for order in orders]
    total = Counter(orders_order).most_common()
    total_set = [item[0] for item in total]
    return set(total_set) - set(personal_set)