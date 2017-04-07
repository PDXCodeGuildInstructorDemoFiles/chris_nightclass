def change(amount):
    change_dict = {
        'quarters': 0,
        'dimes': 0,
        'nickels': 0,
        'pennies': 0
        }
    while amount > 0:
        if amount >= 25:
            change_dict['quarters'] += 1
            amount -= 25
        elif amount >= 10:
            change_dict['dimes'] += 1
            amount -= 10
        elif amount >= 5:
            change_dict['nickels'] += 1
            amount -= 5
        elif amount >= 1:
            change_dict['pennies'] += 1
            amount -= 1

    print('Your change is {} quarters, {} dimes, {} nickels and {} pennies.'.format(change_dict['quarters'], change_dict['dimes'], change_dict['nickels'], change_dict['pennies']))


change(123)
change(12)
change(100)
change(7)
