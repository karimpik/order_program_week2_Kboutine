# Program :  Lesson 2 order program
#Programmer : Karim Boutine
#Date : 10/04/2022
# Purpose : The purpose of this program is to create a basic order form

#input

name = "Karim Boutine"

# explicit declartions 
potato_item = str("potato")
potato_qty = int(1)
potato_price = float(.6)

# implicit declarations
chips_item = "chips"
chips_qty = 3
chips_price = 1

peanut_item = "peanuts"
peanut_qty = 2
peanut_price = 0.5
# ProcessLookupError
potato_total = potato_qty * potato_price
chips_total = chips_qty * chips_price
peanut_total = peanut_qty * peanut_price

order_total = chips_total + potato_total + peanut_total
#   output
print("Order for {}".format(name))
print()
print("item Name Price Qty Total")
print("1. {}      {}       {}   {}".format(potato_item,potato_qty,potato_price,potato_total))
print("2. {}       {}       {}      {}".format(chips_item, chips_qty, chips_price, chips_total))
print("3. {}     {}       {}  {}".format(peanut_item, peanut_qty, peanut_price, peanut_total ))
print("Total            ${}".format(order_total))