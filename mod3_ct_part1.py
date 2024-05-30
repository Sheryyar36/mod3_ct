# Part 1

menu = {'burger': 4.00, 'lettuce, tomato, onion': 0.00, 'cheese': 0.50, 'grilled mushrooms': 0.50,
        'grilled onions': 0.50, 'extra patty': 2.00, 'extra cheese': 1.00}

print('Welcome to Burger Joint!')
print('\nPlease take a look at our menu:')
for i in menu:
    print('\n{}: ${:.2f}'.format(i, menu[i]))


def order():
    ordering = True
    ordered = ['burger']

    while ordering:
        ordered.append(input('\nWhat would you like on your burger? (type "end" to end order)'))
        if (ordered[len(ordered) - 1]) not in menu and ((ordered[len(ordered) - 1]) != 'end'):
            ordered.pop(len(ordered) - 1)
            print('That is not on the menu, please try again.')
        elif (ordered[len(ordered) - 1] == 'end'):
            ordered.pop(len(ordered) - 1)
            ordering = False

    total = 0

    print('\nYou ordered:')
    print('______________')
    for i in ordered:
        print('\n{} : ${:.2f}'.format(i, menu[i]))
        total = total + menu[i]
    print('______________')
    tip = total * 0.18
    tax = (total + tip) * 0.07
    grand_total = total + tip + tax
    return (print('\ntotal: ${:.2f}'.format(total)), print('18 % tip: ${:.2f}'.format(tip)), print('tax : ${:.2f}'.format(tax)),
            print('______________'), print('\ngrand total: ${:.2f}'.format(grand_total))), print('______________'), print('\nThank you for dining with us!')


order()
