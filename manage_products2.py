products = {'computer': [1000, 20],
            'printer': [500, 10],
            'monitor': [200, 15],
            'mouse': [50, 100]}
        
while True:
    print('1. Show products')
    print('2. Buy product')
    print('3. Edit price')
    print('4. Exit')

    choice = input('Enter your choice: ')
    if choice == '1':
        for name in products:
            print(f'{name} - ${products[name][0]} - #{products[name][1]} items')
    elif choice == '2':
        name = input('Enter product to buy: ')
        if name not in products:
            print(f'Product {name} does not exist')
        else:
            quantity = int(input('Enter quantity to buy: '))
            if quantity > products[name][1]:
                print(f'Not enough items. Only {products[name][1]} items left')
            else:
                payment = quantity * products[name][0]
                print(f'You have to pay ${payment}')
                products[name][1] -= quantity
                print(f'You bought {quantity} items of {name}')
    elif choice == '3':
        name = input('Enter product to edit: ')
        if name not in products:
            print(f'Product {name} does not exist')
        else:
            new_price = int(input('Enter new price: '))
            products[name][0] = new_price
            print(f'Price of {name} changed to ${new_price}')
    elif choice == '4':
        break
    else:
        print('Invalid choice')