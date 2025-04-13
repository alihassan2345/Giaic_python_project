fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
total_price=0
for fruit in fruits:
    price = fruits[fruit]
    amount_bought = int(input(f'How many {fruit} do you want to buy? '))
    total_cost = price * amount_bought
    print(f'The total cost of {amount_bought} {fruit} is {total_cost}')
    total_price += total_cost
print(f'The total cost of all fruits is {total_price}')