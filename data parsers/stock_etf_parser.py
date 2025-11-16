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
                                            'Open': round(float(line[1]), 2),
                                            'High': round(float(line[2]), 2),
                                            'low': round(float(line[3]), 2),
                                            'AdjClose': round(float(line[5]), 2),
                                            'Volume': int(line[6]),       
                                        }
                except ValueError:
                    continue

    return price_datas

def main():
    stock_prices = stock_price_data('archive/stocks/*.csv')
    print(stock_prices['AMD']['2020-04-01'])

    etf_prices = stock_price_data('archive/etfs/*.csv')
    print(etf_prices['AGND']['2020-04-01'])


if __name__ == '__main__':
    main()








