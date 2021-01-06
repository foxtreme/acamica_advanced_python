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

    def __getattribute__(self, item):
        print("Getting: ", item)
        return super().__getattribute__(item)

    def __getattr__(self, item):
        print("Getting attribute which doesn't exists: ", item)

    def __setattr__(self, key, value):
        names = ('id', 'account', 'purchased_quantity', 'name', 'quantity', 'unit', 'price', 'category')
        if key not in names:
            raise AttributeError("No attribute {}".format(key))
        print("Setting {} for {}".format(value, key))
        super().__setattr__(key, value)

    def __delattr__(self, item):
        print("Deleting: ", item)
        super().__delattr__(item)

    @property
    def subtotal(self):
        return self.purchased_quantity * self.price

    def __repr__(self):
        return "PurchasedItem("+str(self.__dict__)+")"


class ReadOnly(object):
    """
    Usage:
    p = PurchasedItem("a", "b", 12, "c", "d", "e", 12.1, "f")
    proxy = ReadOnly(p)
    p.price = 100.1  => AttributeError: Read Only
    """
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, item):
        return getattr(self._obj, item)

    def __setattr__(self, key, value):
        if key == "_obj":
            super().__setattr__(key, value)
        else:
            raise AttributeError("Read Only")


class ShoppingCart(object):
    def __init__(self):
        self.items = []

    def __getattr__(self, item):
        return getattr(self.items, item)

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