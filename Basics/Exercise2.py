#You have a shop selling buns for $2.40 each.  A customer comes in with $15, and would like to buy as many buns as possible.

#Complete the code to calculate how many buns the customer can afford.

bun_price = 2.40
customer_money = 15.00

# Use integer division (//) to get the whole number of buns
buns_affordable = int(customer_money // bun_price)

print("The customer can buy", buns_affordable, "buns.")
