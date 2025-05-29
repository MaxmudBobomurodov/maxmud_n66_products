from core.database_settings import execute_query

def show_all_products():
    query = "SELECT * FROM products ORDER BY id;"
    return execute_query(query=query, fetch="all")

def add_products(name,quantity):
    query = "INSERT INTO products (name, quantity) VALUES (%s, %s);"
    execute_query(query, (name, quantity))
    print("Added products successfully")

def delete_products(product_id):
    query = "DELETE FROM products WHERE id = %s;"
    execute_query(query,(product_id,))
    print("Deleted products successfully")

def update_status(product_id: int, status: bool):
    query = "UPDATE products SET status = %s WHERE id = %s;"
    execute_query(query, (status, product_id))
    print("Updated status successfully")