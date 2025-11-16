import csv
from icecream import ic as print

def stock_data() -> dict[dict]:
    '''Parse and Return Ticker Data'''
    stocks = {}
    filename = 'archive/symbols_valid_meta.csv'

    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile) # reader object
        next(csv_reader)                 # skip header

        for line in csv_reader:
            ticker = line[1]

            stocks[ticker] = {
                            'StockID': ticker,
                            'SecurityName': line[2],
                            'ListingExchange': line[3],
                            'MarketCategory': line[4] if line[4].strip() else None,
                            'ETF': line[5].strip().isupper() == 'Y'
                        }
            
    return stocks

def main():
    x = stock_data()
    print(x['AMD'])
    print(x['AMD']['SecurityName'])

if __name__ == "__main__":
    main()