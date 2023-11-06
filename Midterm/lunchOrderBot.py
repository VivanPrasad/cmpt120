# lunchOrderBot.py
#
# Description: Get the total cost of the user's lunch order
#
# Name: M. V. Prasad
# Date: October 27th, 2023 (Friday)

print("Lunch Menu:\n \
Sandwich -> $5\n \
Salad -> $4\n \
Juice -> $2\n \
Fruit -> $1")

item_costs = {"Sandwich":5,"Salad":4,
    "Juice":2,"Fruit":1}

#Running sum of total cost
total_cost = 0
tax = 1.15

print("From the lunch menu, would you like...")
for item in item_costs.keys():
    response = input(f"a {item} (y/n)? ")
    if response.lower() == "y":
        total_cost += item_costs[item]
    elif response.lower() != "n":
        print("I'm going to assume that's a no.")

print(f"Your cost for your lunch is ${total_cost}.")
print(f"With tax, the total cost will be ${total_cost*tax}.")