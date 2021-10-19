import sys 

def mainMenu(): 
    while True:
        print(''' 
        --- Main Menu ---

        1 View Products
        2 Add item to Basket
        3 Remove item from Basket
        4 View Basket
        5 Exit
        ''')

        selection = input('Please select a number for action:')

        if selection == '1':
            displayProducts() 
        elif selection == '2':
            pass
        elif selection == '3':
            pass
        elif selection == '4':
            pass
        elif selection == '5':
            sys.exit()
        else:
            print(input('Your selection was invalid, please select a number for action:'))

products = {'Apples': 1.29, 'Bananas': 0.99, 'Bread': 1.50, 'Sausages': 2.50, 'Eggs': 1.00, 
'Milk': 0.85, 'Potatoes': 0.60, 'Carrots': 1.15, 'Broccoli': 0.90}

def displayProducts():
    print()
    print('--- Products ---' + '\n')
    for item in products:
        print(f'{item} : {products[item]}')

mainMenu()