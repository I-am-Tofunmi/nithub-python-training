def my_discount():
    price = int(input("Enter the price of the product: "))
    discount = int(input("Enter the discount of the product: "))
    actual_discount = 100 - discount
    total_price = price * actual_discount / 100
    return (f"The total price is {total_price}")
    
print(my_discount())