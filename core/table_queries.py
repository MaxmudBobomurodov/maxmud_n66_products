from core.database_settings import execute_query

products = """
        CREATE TABLE IF NOT EXISTS products(
            id          SERIAL PRIMARY KEY,
            name        VARCHAR(255) NOT NULL UNIQUE,
            quantity    VARCHAR(255) NOT NULL,
            status      BOOLEAN DEFAULT FALSE
        );
        
        """

def initializing_table():
    execute_query(query=products)