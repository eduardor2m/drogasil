from tinydb import TinyDB, where
from pathlib import Path
import productClass


dbPath = Path(__file__).parent / 'db.json'
db = TinyDB(dbPath, indent=4, sort_keys=True, separators=(',', ': '))

while True:
    opction = input('''
  1. Add product
  2. List products
  3. Delete product
  4. Update product
  5. Buy product
  6. Replenish Stock
  7. Exit
  ''')

    if opction == '1':
        name = input('Name: ')
        price = float(input('Price: '))
        quantity = int(input('Quantity: '))

        productObject = productClass.Product(name, price, quantity)
        db.insert(productObject.as_dict())

    elif opction == '2':
        for product in db:
            print(product)

    elif opction == '3':
        name = input('Name: ')
        db.remove(where('name') == name)

    elif opction == '4':
        name = input('Name: ')
        price = float(input('Price: '))
        quantity = int(input('Quantity: '))

        product = productClass.Product(name, price, quantity)
        db.update(product.as_dict(), where('name') == name)

    elif opction == '5':
        name = input('Name: ')
        quantity = int(input('Quantity: '))

        product = db.search(where('name') == name)[0]
        product['quantity'] -= quantity
        db.update(product, where('name') == name)

    elif opction == '6':
        name = input('Name: ')
        quantity = int(input('Quantity: '))

        product = db.search(where('name') == name)[0]
        product['quantity'] += quantity
        db.update(product, where('name') == name)

    elif opction == '7':
        break

    else:
        print('Invalid option')
