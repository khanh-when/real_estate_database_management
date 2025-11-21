import mariadb
from data_parsers.stock_data_parser import stock_data
from data_parsers.price_data_parser import price_data
from data_parsers.reformat_data import reformat

def connection(db_name):
    '''Establish Database Connection to MariaDB'''

    try:
        return mariadb.connect(
                user = 'root',
                password = '2123<>69',
                host = 'localhost',
                port = 3306,
                database = db_name,
                autocommit = True
            ) 
    
    except mariadb.Error as e:
        print(f"Error: MariaDB Connection {e}")
        raise mariadb.Error
    

def insert_stocks(conn, data, type=1):
    '''Insert a New Stock(s) into the Stocks Table'''
    query = "INSERT INTO Stocks VALUES (?, ?, ?, ?, ?)"

    if type == 1:

        try:
            with conn.cursor() as cursor:
                cursor.execute(query, (data[0], data[1], data[2], data[3], data[4]))
            print(f"Stock: {data[0]} is successfully added to the Stock Table.")

        except mariadb.Error as e:
            print(f"Error: Insert - {e}")
            raise mariadb.Error
        
    if type == 2:

        try:
                
            with conn.cursor() as cursor:
                cursor.executemany(query, data)
            print(f"Successfully Inserted All Stocks into the Database.")

                
        except mariadb.Error as e:
            print(f"Error: MariaDB Several Insertions {e}")
            raise mariadb.Error


def main():

    stocksData = stock_data()
    formatted = reformat(stocksData, type=1)

    try:
        conn = connection('stock_market')
        insert_stocks(conn, formatted, type=2)

    except Exception as e:
        print(f'Error: {e}')

    finally:
        conn.close()



if __name__ == '__main__':
    main()

