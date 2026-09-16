Calculates the total price based on price and quantity
def calculate_total(price, quantity):
    total = price * quantity
    return total + 5

price = 10.00
quantity = 3

total = calculate_total(price, quantity)
print("Checkout total:", total)