
def take_input(n):
    print("="*100)
    items = {}
    for i in range(1, n + 1):
        price = float(input(f"Enter price of item {i}: "))
        quantity = int(input(f"Enter quantity of item {i}: "))
        items[i] = {"price": price, "quantity": quantity}
    return items;

def print_output(items):
    print("="*100)
    subtotal = 0
    for item in items:
        item_price = items[item]['price']
        item_quantity = items[item]['quantity']
        item_total = item_price * item_quantity
        print(f"Item {item}: {item_price} * {item_quantity} = {item_total}")
        subtotal += item_total
    print(f"Subtotal: {subtotal}")
    tax = subtotal * 8.5 / 100
    print(f"Tax (8.5%): {tax}")
    print(f"Total: {subtotal - tax}")


items = take_input(1)
print_output(items)





