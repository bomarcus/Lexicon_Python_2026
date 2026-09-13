# Lab-1_B-2

# ask user to input price and save in variable called price. convert to float.
price = float(input("Give me a price! "))
# ask user for input  - discount percentage and create variable. convert to int.
discount = int(input("How large of a discount percentage would you like? "))
# calculate amount to discount from price
discount_amount = price * (discount / 100)
# calculate final price
final_price = price - discount_amount
# print final price with two decimals.``
print("Your final price is:", round(final_price, 2))