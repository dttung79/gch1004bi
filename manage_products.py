products = {} # 1 product includes id and name
id = 0
while True:
    print('1. Add product')
    print('2. Show products')
    print('3. Delete product')
    print('4. Edit product')
    print('5. Exit')

    choice = input('Enter your choice: ')
    if choice == '1':
        product_name = input('Enter product name: ')
        if product_name in products.values():
            print(f'Product {product_name} already exists')
        else:
            products[id] = product_name
            id += 1
    elif choice == '2':
        for id, name in products.items():
            print(f'{id} - {name}')
    elif choice == '3':
        del_id = int(input('Enter product id to delete: '))
        if del_id not in products:
            print(f'Product with id {del_id} does not exist')
        else:
            del products[del_id]
            print(f'Product {del_id} deleted')
    elif choice == '4':
        edit_id = int(input('Enter product id to edit: '))
        if edit_id not in products:
            print(f'Product with id {edit_id} does not exist')
        else:
            new_name = input('Enter new name: ')
            products[edit_id] = new_name
            print(f'Product {edit_id} changed to {new_name}')
    elif choice == '5':
        break
    else:
        print('Invalid choice')