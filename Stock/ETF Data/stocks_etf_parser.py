import csv
import glob
from icecream import ic as print

def stock_price_data(path: str) -> dict[dict]:
    '''Parse and Return data of Common Stocks / ETFs'''
    price_datas = {}
    file_path = path
    all_files = glob.glob(file_path, recursive=True)


    for file in all_files:
        with open(file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader) # skip header

            ticker = file.split('/')[-1].strip('.csv') # parse for filename
            price_datas[ticker] = {}

            for line in csv_reader:
                date = line[0]

                try:
                    price_datas[ticker][date] = {
                                            'Date': date,
                                            'Open': float(line[1]),
                                            'High': float(line[2]),
                                            'low': float(line[3]),
                                            'AdjClose': float(line[5]),
                                            'Volume': float(line[6]),       
                                        }  
                except ValueError:
                    continue

    return price_datas

def main():
    stock_prices = stock_price_data('archive/stocks/*.csv')
    print(len(stock_prices))

    etf_prices = stock_price_data('archive/etfs/*.csv')
    print(etf_prices)


if __name__ == '__main__':
    main()








