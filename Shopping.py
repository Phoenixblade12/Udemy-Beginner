# Money in wallet
money_in_wallet = 40

print(money_in_wallet)

# Nett price of treats
treats_price = 7.50

# Calculate tax
sales_tax = 0.2 * treats_price

#Calculate gross proce (adding tax to the net price of treats)
treats_price += sales_tax

#Updating money in wallet
money_in_wallet -= treats_price

print(money_in_wallet)
