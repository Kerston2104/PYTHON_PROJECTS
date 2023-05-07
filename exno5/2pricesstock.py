# Follow the steps bellow: -Create a new dictionary called prices using {} format like

# the example above.
# ● Put these values in your prices dictionary:
# "banana": 4,
# "apple": 2,
# "orange": 1.5,
# "pear": 3
# ● Loop through each key in prices. For each key, print out the key along with
# its price and stock information. Print the answer in the following format:
# apple
# price: 2
# stock: 0
# ● Let's determine how much money you would make if you sold all of your
# food.
# o Create a variable called total and set it to zero.
# o Loop through the prices dictionaries. For each key in prices, multiply
# the number in prices by the number in stock. Print that value into the
# console and then add it to total.
# o Finally, outside your loop, print total.


prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
prices["banana_stock"] = 6
prices["apple_stock"] = 0
prices["orange_stock"] = 32
prices["pear_stock"] = 15
for item, price in prices.items():
    if "stock" not in item:
        print(item)
        print("price:", price)
        print("stock:", prices[item+"_stock"])
total = 0
for item, price in prices.items():
    if "stock" in item:
        total += price * prices[item]
        print("Total value for", item.split("_")[0], ":", price * prices[item])
print("Total value for all items:", total)

















# repo created by kerston2104