import mariadb

def connection(db_name):
    '''Establish Database Connection to MariaDB'''

    try:
        return mariadb.connect(
                user = 'root',
                password = '2123<>69',
                host = 'localhost',
                port = 3306,
                database = db_name
            )
    except mariadb.Error as e:
        print(f"Error: MariaDB Connection {e}")
        raise mariadb.Error
 
def create_table(conn, tbl_name: str):
    query = f"""
    CREATE TABLE IF NOT EXISTS {tbl_name}(
        id INT,
        name VARCHAR(20)
    )
    """

    try:
        with conn.cursor() as cur:
            cur.execute(query, (tbl_name,))
        print("Table was created!")
    
    except mariadb.Error as e:
        print(f"Error: Table - {e}")

def main():
    try:
        conn = connection('stock_market')
        create_table(conn, 'cool')

    except Exception as e:
        print(f'Error: {e}')

    finally:
        conn.close()


if __name__ == '__main__':
    main()

