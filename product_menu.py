from product_functions import *

def menu():
    print("""
    1.show products
    2.add products
    3.delete products
    4.change status
    5.exit
    """)
    choice = input("enter your choice:")
    if choice == '1':
        products = show_all_products()
        if not products:
            print("No products found")

        for i in products:
            if i['status']:
                status = "bought"
            else:
                status = "not bought"
            print(f"id: {i['id']}\nname: {i['name']}\nstatus: {status}")


    elif choice == '2':
        name = input("enter product name:")
        quantity = int(input("enter product quantity:"))

        if name and quantity:
            add_products(name, quantity)
        else:
            print("name and quantity are required")


    elif choice == '3':
        try:
            product_id = int(input("Enter product ID to delete: "))
            delete_products(product_id)
        except ValueError:
            print("Invalid ID format.")


    elif choice == '4':
        try:
            product_id = int(input("Enter product ID: "))
            status_input = input("Is it bought? (yes/no): ").strip().lower()
            if status_input == "yes":
                status = True
            elif status_input == "no":
                status = False
            else:
                print("Please enter 'yes' or 'no'")
                return menu()
            update_status(product_id, status)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


    elif choice == '5':
        print("exit")
        return
    else:
        print("invalid choice")
    menu()
