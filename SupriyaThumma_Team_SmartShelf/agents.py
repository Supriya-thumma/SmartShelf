# agents.py
class StoreAgent:
    def __init__(self, store_id):
        self.store_id = store_id
        self.inventory = {}

    def check_inventory(self):
        return self.inventory

    def update_inventory(self, product, quantity):
        self.inventory[product] = self.inventory.get(product, 0) + quantity


class WarehouseAgent:
    def __init__(self):
        self.inventory = {}

    def restock(self, product, quantity):
        self.inventory[product] = self.inventory.get(product, 0) + quantity


class SupplierAgent:
    def supply(self, product, quantity):
        print(f"Supplying {quantity} of {product}")


class CustomerAgent:
    def provide_feedback(self, product):
        print(f"Customer feedback for {product}")