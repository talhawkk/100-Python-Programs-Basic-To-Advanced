class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_product(self):
        print(f"Product ID: {self.product_id}, Name: {self.name}, Price: {self.price}")


class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product):
        self.cart_items.append(product)

    def remove_product(self, product):
        if product in self.cart_items:
            self.cart_items.remove(product)
        else:
            print("Product not in cart.")

    def calculate_total(self):
        total = sum(product.price for product in self.cart_items)
        return total

    def display_cart(self):
        if not self.cart_items:
            print("Your shopping cart is empty.")
        else:
            for product in self.cart_items:
                product.display_product()
            print(f"Total Cost: {self.calculate_total():.2f}")


# Example usage
cart = ShoppingCart()
product1 = Product(1, "Laptop", 80000)
product2 = Product(2, "Smartphone", 50000)

cart.add_product(product1)
cart.add_product(product2)

cart.display_cart()

cart.remove_product(product1)
cart.display_cart()
