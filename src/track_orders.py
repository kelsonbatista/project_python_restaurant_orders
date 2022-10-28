from collections import Counter


class TrackOrders:
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        self._data.append({"customer": customer, "order": order, "day": day})

    def get_most_ordered_dish_per_customer(self, customer):
        items = []
        for order in self._data:
            if order["customer"] == customer.lower():
                items.append(order["order"])
        result = Counter(items).most_common()
        return result[0][0]

    def get_never_ordered_per_customer(self, customer):
        items = []
        for order in self._data:
            if order["customer"] == customer.lower():
                items.append(order["order"])
        personal = Counter(items).most_common()
        personal_set = [item[0] for item in personal]
        orders_order = []
        for order in self._data:
            orders_order.append(order["order"])
        total = Counter(orders_order).most_common()
        total_set = [item[0] for item in total]
        return set(total_set) - set(personal_set)

    def get_days_never_visited_per_customer(self, customer):
        personal_weekday = [order["day"]
                            for order in self._data
                            if order["customer"] == customer.lower()]
        personal = Counter(personal_weekday).most_common()
        personal_set = [item[0] for item in personal]
        orders_order = [order["day"] for order in self._data]
        total = Counter(orders_order).most_common()
        total_set = [item[0] for item in total]
        return set(total_set) - set(personal_set)

    def get_busiest_day(self):
        orders_order = [order["day"] for order in self._data]
        total = Counter(orders_order).most_common()
        return total[0][0]

    def get_least_busy_day(self):
        orders_order = [order["day"] for order in self._data]
        total = Counter(orders_order).most_common()
        return total[-1][0]
