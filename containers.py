import csv


class PurchasedItem(object):

    counter = 0

    def __init__(
            self,
            id,
            account,
            purchased_quantity,
            name,
            quantity,
            unit,
            price,
            category
    ):
        PurchasedItem.counter += 1
        self.id = id
        self.account = account
        self.purchased_quantity = purchased_quantity
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.price = price
        self.category = category

    def subtotal(self):
        return self.purchased_quantity * self.price

    def change_price(self, price):
        self.price = price

    def __repr__(self):
        return "PurchasedItem("+str(self.__dict__)+")"


def read_shopping_data(filename):
    """
    Buils a list of rows from a csv file
    :param filename: string, the file name
    :return: list, the list of PurchasedItems objects
    """
    data = []
    with open(filename) as f:
        rows = csv.reader(f)
        next(f)
        for row in rows:
            row[2] = int(row[2])
            row[6] = float(row[6])

            item = PurchasedItem(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7]
            )
            data.append(item)
    return data


class ShoppingCart(object):
    def __init__(self):
        self.items = []

    @classmethod
    def from_csv(cls, filename):
        self = cls()
        with open(filename) as f:
            rows = csv.reader(f)
            next(rows)
            for row in rows:
                row[2] = int(row[2])
                row[6] = float(row[6])

                obj = PurchasedItem(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7]
                )
                self.items.append(obj)
        return self

    def total(self):
        return sum([item.purchased_quantity * item.price for item in self.items])

    def __repr__(self):
        return "\n".join([str(item.__dict__) for item in self.items])

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        if isinstance(index, str):
            filtered_items = [item for item in self.items if index in item.name.lower()]
            new_cart = self.__class__()
            new_cart.items = filtered_items
            return new_cart
        else:
            return self.items[index]

    def __iter__(self):
        return self.items.__iter__()
