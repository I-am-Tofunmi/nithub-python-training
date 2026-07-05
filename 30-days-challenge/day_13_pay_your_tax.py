# Pay Your Tax
def your_vat():
    while True:
        try:
            price = int(input("Enter the price of the item: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.") 
            continue
    
    while True:
        try:
            vat_rate = int(input("Enter the VAT rate ( as a percentage): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
    
    result = price + (price * vat_rate / 100)
    return result

print("The total price including VAT is:", your_vat())