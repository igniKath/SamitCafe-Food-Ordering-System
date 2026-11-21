class MenuItem:
    

    def __init__(self, item_id, name, price, image="placeholder.jpg", available=True):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.image = image          
        self.available = available


class Order:
    
    def __init__(self):
        self.items = {}  

    def add_item(self, menu_item, quantity):
        if not menu_item.available:
            raise ValueError(f"Sorry, {menu_item.name} is not available.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a whole number greater than 0.")

        if menu_item.item_id in self.items:
            self.items[menu_item.item_id]["qty"] += quantity
        else:
            self.items[menu_item.item_id] = {"item": menu_item, "qty": quantity}

    def remove_item(self, item_id):
        if item_id not in self.items:
            raise ValueError("That item is not in your order.")
        del self.items[item_id]

    def get_lines(self):
        
        return [
            (entry["item"], entry["qty"], entry["item"].price * entry["qty"])
            for entry in self.items.values()
        ]

    def calculate_total(self):
        return sum(line_total for _, _, line_total in self.get_lines())

    def reset(self):
        self.items.clear()



MENU = {
    "1": MenuItem("1", "Strawberry Glaze Donut", 45,  "strawberry-donut.jpg"),
    "2": MenuItem("2", "Iced Caramel Latte",     120, "caramel-latte.jpg"),
    "3": MenuItem("3", "Cheesy Ham Sandwich",    85,  "ham-sandwich.jpg"),
    "4": MenuItem("4", "Choco Lava Cake",        95,  "choco-lava.jpg"),
    "5": MenuItem("5", "Berry Cream Frappe",     130, "berry-frappe.jpg"),
    "6": MenuItem("6", "Matcha Cheesecake",      110, "matcha-cheesecake.jpg", available=False),
}