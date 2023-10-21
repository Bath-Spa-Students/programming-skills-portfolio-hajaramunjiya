usb_price = 6  # Price of each USB stick in pounds
total_money = 50  # Total money in pounds
#We define the price of each USB stick as usb_price and the total money she has as total_money.

# Calculate the number of USB sticks she can buy
num_usb_sticks = total_money // usb_price
#We use the floor division (//) operator to calculate the maximum number of USB sticks she can buy with the given money.

# Calculate the remaining money after buying the USB sticks
remaining_money = total_money % usb_price
#We use the modulus (%) operator to calculate the remaining money after buying the USB sticks.

# Display the results
print("Number of USB sticks she can buy:", num_usb_sticks)
print("Remaining money in pounds:", remaining_money)
#Finally, we print the number of USB sticks she can buy and the remaining money