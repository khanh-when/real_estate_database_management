import mariadb, datetime
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
            print(f"Successfully Inserted All Stocks into the Stock Table.")

        except mariadb.Error as e:
            print(f"Error: MariaDB Several Insertions {e}")
            raise mariadb.Error

def insert_prices(conn, data, type=1):
    '''Insert New Price Data(s) into the PriceData Table'''
    query = "INSERT INTO PriceData VALUES (?, ?, ?, ?, ?, ?, ?)"

    if type == 1:

        try:
            with conn.cursor() as cursor:
                cursor.execute(query, ('A', datetime.date(1999, 11, 18), 32.55, 35.77, 28.61, 27.07, 62546300))
            print(f'Stock: {data[0]} | Date: {data[0]} | Successfully added to the PriceData Table.')
        
        except mariadb.Error as e:
            print(f"Error: Insert - {e}")
            raise mariadb.Error
        
    if type == 2:
        pass

def main():
    # share_data = reformat(stock_data(), type=1)
    # for item in share_data:
    #     print(item)

    share_prices = reformat(price_data('archive/stocks/*.csv'), type=2)

    for item in share_prices:
        print(item)
        break

    # etf_prices = reformat(price_data('archive/etfs/*.csv'), type=2)

    try:

        conn = connection('stock_market') # create cursor connection to stock_market db
        # insert_stocks(conn, formatted, type=2) # insert all Stock/ETF .CSV metadata

        insert_prices(conn, ['ok', 10], type=1)

    except Exception as e:
        print(f'Error: {e}')

    finally:
        conn.close()



if __name__ == '__main__':
    main()

