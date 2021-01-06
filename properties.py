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

    @property
    def subtotal(self):
        return self.purchased_quantity * self.price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if value < 0:
            raise ValueError("Price must be >= 0")
        self._price = value

    def __repr__(self):
        return "PurchasedItem("+str(self.__dict__)+")"
