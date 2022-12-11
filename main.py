from tinydb import TinyDB, where
from pathlib import Path
import productClass
import clientClass
import employeeClass
import salesClass

dbPathProducts = Path(__file__).parent / 'database/products.json'
dbProducts = TinyDB(dbPathProducts, indent=4,
                    sort_keys=True, separators=(',', ': '))

dbPathClients = Path(__file__).parent / 'database/clients.json'
dbClients = TinyDB(dbPathClients, indent=4,
                   sort_keys=True, separators=(',', ': '))

dbPathEmployees = Path(__file__).parent / 'database/employees.json'
dbEmployees = TinyDB(dbPathEmployees, indent=4,
                     sort_keys=True, separators=(',', ': '))

dbPathSales = Path(__file__).parent / 'database/sales.json'
dbSales = TinyDB(dbPathSales, indent=4, sort_keys=True, separators=(',', ': '))


opt = input(
    'Section: \n 1. Products \n 2. Clients \n 3. Employee \n 4. Sales \n 5. Exit \n'
)

if opt == '1':

    while True:
        opction = input('''
    1. Add product
    2. List products
    3. Delete product
    4. Update product
    5. Exit
    ''')

        if opction == '1':
            name = input('Name: ')
            for product in dbProducts:
                if product['name'] == name:
                    print('Product already exists')
                    exit()
            price = float(input('Price: '))
            quantity = int(input('Quantity: '))

            productObject = productClass.Product(name, price, quantity)
            dbProducts.insert(productObject.as_dict())

        elif opction == '2':
            for product in dbProducts:
                print(product)

        elif opction == '3':
            name = input('Name: ')
            dbProducts.remove(where('name') == name)

        elif opction == '4':
            name = input('Name: ')
            for product in dbProducts:
                if product['name'] == name:
                    continue

                else:
                    print('Product not found')
                    exit()
            price = float(input('Price: '))
            quantity = int(input('Quantity: '))

            product = productClass.Product(name, price, quantity)
            dbProducts.update(product.as_dict(), where('name') == name)

        elif opction == '5':
            break

        else:
            print('Invalid option')

elif opt == '2':

    while True:
        opction = input('''
        1. Add client
        2. List clients
        3. Delete client
        4. Update client
        5. Exit
        ''')

        if opction == '1':
            name = input('Name: ')
            for client in dbClients:
                if client['name'] == name:
                    print('Client already exists')
                    exit()
            phone = input('Phone: ')
            email = input('Email: ')

            clientObject = clientClass.Client(name, phone, email)
            dbClients.insert(clientObject.as_dict())

        elif opction == '2':
            for client in dbClients:
                print(client)

        elif opction == '3':
            name = input('Name: ')
            for client in dbClients:
                if client['name'] == name:
                    continue

                else:
                    print('Client not found')
                    exit()
            dbClients.remove(where('name') == name)

        elif opction == '4':
            name = input('Name: ')
            for client in dbClients:
                if client['name'] == name:
                    continue

                else:
                    print('Client not found')
                    exit()
            phone = input('Phone: ')
            email = input('Email: ')

            client = clientClass.Client(name, phone, email)
            dbClients.update(client.as_dict(), where('name') == name)

        elif opction == '5':
            break

        else:
            print('Invalid option')

elif opt == '3':

    while True:
        opction = input('''
            1. Add employee
            2. List employees
            3. Delete employee
            4. Update employee
            5. Exit
            ''')

        if opction == '1':
            name = input('Name: ')
            for employee in dbEmployees:
                if employee['name'] == name:
                    print('Employee already exists')
                    exit()
            password = input('Password: ')
            office = input('Office: ')

            employeeObject = employeeClass.Employee(name, password, office)
            dbEmployees.insert(employeeObject.as_dict())

        elif opction == '2':
            for employee in dbEmployees:
                print(employee)

        elif opction == '3':
            name = input('Name: ')
            for employee in dbEmployees:
                if employee['name'] == name:
                    continue

                else:
                    print('Employee not found')
                    exit()
            dbEmployees.remove(where('name') == name)

        elif opction == '4':
            name = input('Name: ')
            for employee in dbEmployees:
                if employee['name'] == name:
                    continue

                else:
                    print('Employee not found')
                    exit()
            password = input('Password: ')
            office = input('Office: ')

            employee = employeeClass.Employee(name, password, office)
            dbEmployees.update(employee.as_dict(), where('name') == name)

        elif opction == '5':
            break

        else:
            print('Invalid option')

elif opt == '4':

    while True:
        opction = input('''
                1. Add sale
                2. List sales
                3. Delete sale
                4. Update sale
                5. Exit
                ''')

        if opction == '1':
            nameCliente = str(input('Name Client: '))
            for client in dbClients:
                if client['name'] == nameCliente:
                    client = client['name']
                    continue

                else:
                    print('Client not found')
                    exit()

            nameEmployee = str(input('Name Employee: '))
            for employee in dbEmployees:
                if employee['name'] == nameEmployee:
                    employee = employee['name']
                    continue

                else:
                    print('Employee not found')
                    exit()

            nameProduct = str(input('Name Product: '))
            for product in dbProducts:
                if product['name'] == nameProduct:
                    product = product['name']
                    continue

                else:
                    print('Product not found')
                    exit()

            quantity = int(input('Quantity: '))
            for product in dbProducts:
                if product['quantity'] >= quantity:
                    product['quantity'] -= quantity
                    continue

                else:
                    print('Insufficient quantity')
                    exit()
            saleObject = salesClass.Sale(
                nameCliente, nameEmployee, nameProduct, quantity)
            dbSales.insert(saleObject.as_dict())

        elif opction == '2':
            for sale in dbSales:
                print(sale)

        elif opction == '3':
            nameCliente = str(input('Client: '))
            dbSales.remove(where('client') == nameCliente)

        elif opction == '4':
            nameClient = str(input('Client: '))

            nameEmployee = str(input('Employee: '))
            nameProduct = str(input('Product: '))
            quantity = int(input('Quantity: '))

            sales = salesClass.Sale(
                nameClient, nameEmployee, nameProduct, quantity)
            dbSales.update(sales.as_dict(), where('client') == client)

        elif opction == '5':
            break

        else:
            print('Invalid option')
