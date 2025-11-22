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
    
def insert_stocks(conn, data, type):
    '''Insert a New Stock(s) into the Stocks Table'''
    query = "INSERT INTO Stocks VALUES (?, ?, ?, ?, ?)"

    if type == 1:

        try:
            with conn.cursor() as cursor:
                cursor.execute(query, data)
            print(f"Stock: {data[0]} is successfully added to the Stock Table.")

        except mariadb.Error as e:
            print(f"Error: Insert - {e}")
            raise mariadb.Error
        
    if type == 2:

        try:    
            with conn.cursor() as cursor:
                cursor.executemany(query, data)

        except mariadb.Error as e:
            print(f"Error: Insert - {e}")
            raise mariadb.Error

def insert_prices(conn, data, type):
    '''Insert New Price Data(s) into the PriceData Table'''
    query = "INSERT INTO PriceData VALUES (?, ?, ?, ?, ?, ?, ?)"

    if type == 1:

        try:
            with conn.cursor() as cursor:
                cursor.execute(query, data)
            print(f'Stock: {data[0]} | Date: {data[1]} | Successfully added to the PriceData Table.')
        
        except mariadb.Error as e:
            print(f"Error: Insert - {e}")
            raise mariadb.Error
        
    if type == 2:
        
        try:
            with conn.cursor() as cursor:
                cursor.executemany(query, data)

        except mariadb.Error as e:
            print(f"Error: Insert - {e}")
            raise mariadb.Error

def chunk_data_insert(conn, data, archtype):
    hashmap = {1: insert_stocks,
               2: insert_prices}
    
    for i in range(0, len(data), 1000):
        print(i)
        hashmap[archtype](conn, data[i:i+1000], type=2)
    
    print('All Data Successfully Inserted.')


def main():

    # all stock data in a list[tuple] data structure
    share_data = reformat(stock_data(), type=1) 
    print("All Stocks Datas:", len(share_data)) # 8,049 items

    # all share price data in a list[tuple] data structure
    share_prices = reformat(price_data('archive/stocks/*.csv'), type=2) 
    print("All Share Price Datas:", len(share_prices)) # 17,219,159 items

    print(share_prices[7410])
    print(share_prices[7409])
    
    # keys = [share_prices[i][0] for i in range(2573000, 2574001)]
    # x = stock_data()

    # for item in keys:
    #     if item not in x:
    #         print(item)
    
    # # all etf price data in a list[tuple] data structure
    # etf_prices = reformat(price_data('archive/etfs/*.csv'), type=2)
    # print("All ETF Price Datas:", len(etf_prices)) # 3,905,783 items

    try:
        conn = connection('stock_market') # create cursor connection to stock_market db
        # chunk_data_insert(conn, share_data, archtype=1) # insert all .csv share data metadata
        # chunk_data_insert(conn, share_prices, archtype=2) # insert all .csv share price metadata
        # recursive_batch_insert(conn, etf_prices, type=2) # insert all .csv etf price metadata

    except mariadb.Error as e:
        print(f'Error: {e}')

    finally:
        conn.close()


if __name__ == '__main__':
    main()
