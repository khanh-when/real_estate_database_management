import mariadb
from dataparsers.ticker_data_parser import stock_data
from dataparsers.stock_etf_parser import price_data
from dataparsers.reformat_data import reformat

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


def insert_stock(conn, stock_id: str, security_name: str, listing_exchange: str, marketing_category: str, is_etf: bool):
    '''Insert a New Stock into the Stocks Table'''
    query = "INSERT INTO Stocks(Stock_ID, SecurityName, ListingExchange, MarketCategory, ETF) VALUES (?, ?, ?, ?, ?);"

    try:
        with conn.cursor() as cursor:
            cursor.execute(query, (stock_id, security_name, listing_exchange, marketing_category, is_etf))
        print(f"Stock: {stock_id} is successfully added to the Stock Table.")

    except mariadb.Error as e:
        print(f"Error: Insert - {e}")
        raise mariadb.Error



def main():

    stocksData = stock_data()

    formatted = reformat(stocksData, type=1)

    for i in range(10):
        print(formatted[i])


    # print(stocksData['AMD']['SecurityName'])
    # pricesData = price_data('archive/stocks/*.csv')
    # print(stocksData['AMD'])
    # print(pricesData['AMD']['2020-04-01'])

    try:
        conn = connection('stock_market')

        # insert_stock(conn, x['StockID'], x['SecurityName'], x['ListingExchange'], x['MarketCategory'], x['ETF'])

    except Exception as e:
        print(f'Error: {e}')

    finally:
        conn.close()



if __name__ == '__main__':
    main()

