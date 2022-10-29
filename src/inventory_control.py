from collections import Counter


class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self._data = list()
        self._inventory = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def add_new_order(self, customer, order, day):
        self._data.append({"customer": customer, "order": order, "day": day})
        orders = self.get_orders()
        for item in orders:
            for ingredient in self.INGREDIENTS[item[0]]:
                if ingredient != order:
                    return False

    def get_quantities_to_buy(self):
        personal = self.get_orders()
        for p_order in personal:
            for ingredient in self.INGREDIENTS[p_order[0]]:
                new_value = self._inventory[ingredient]
                self._inventory.update({ingredient: p_order[1] + new_value})
        return self._inventory

    def get_available_dishes(self):
        dishes = set(self.INGREDIENTS.keys())
        orders = self.get_orders()
        orders_ingredients = self.INGREDIENTS[orders[0][0]]
        for dish, ingredients in self.INGREDIENTS.items():
            for ingredient in ingredients:
                if (self.MINIMUM_INVENTORY[ingredient] - orders[0][1]) <= 0 \
                        and ingredient in orders_ingredients \
                        and dish in dishes:
                    dishes.remove(dish)
        return dishes

    def get_orders(self):
        items = list()
        for item in self._data:
            items.append(item["order"])
        return (Counter(items).most_common())
