class Pizza:
    def __init__(self, toppings):
        self.toppings = list(toppings)
    

    def __repr__(self):
        return f"Pizza({self.toppings})"
    

    def add_topping(self, tooping):
        self.toppings.append(tooping)


    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)
    

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomatoes"])
    

    @classmethod
    def prosciutto(cls):
        return cls(["mozzarella", "tomatoes", "ham"])
    

    @staticmethod
    def get_size_in_inches(size):
        """Returns the diameter in inches for common pizza sizes."""
        size_map = {
            "small": 8,
            "medium": 12,
            "large": 16,
            }
        return size_map.get(size, "Unknown size")
    

pizza = Pizza(["cheese", "tomatoes"])
print(pizza)

pizza.add_topping("garlic")
print(pizza)

pizza.remove_topping("cheese")
print(pizza)

print(Pizza.margherita())

print(Pizza.prosciutto())

a_pizza = Pizza.prosciutto()
a_pizza.add_topping("garlic")
print(a_pizza)
print(a_pizza.get_size_in_inches("medium"))
print(a_pizza.get_size_in_inches("small"))
print(a_pizza.get_size_in_inches("little"))
print(a_pizza.get_size_in_inches("big"))