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

    def get_quantities_to_buy(self):
        items = list()
        for order in self._data:
            items.append(order["order"])
        personal = (Counter(items).most_common())
        for p_order in personal:
            for ingredient in self.INGREDIENTS[p_order[0]]:
                self._inventory.update({ingredient: p_order[1]})

        return self._inventory
