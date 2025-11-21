import csv
import glob
from icecream import ic as print
import datetime

def price_data(file_path) -> dict[dict]:
    '''Parse and Return data of Common Stocks / ETFs'''
    
    def process_file(file_path, price_datas):
        '''Store .CSV Price Data of Stocks/ETFs into One Data Dictionary'''

        files = glob.glob(file_path, recursive=True)

        for file in files:

            with open(file, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader) # skip header

                ticker = file.split('/')[-1].strip('.csv') # parse for filename
                price_datas[ticker] = {}

                for line in csv_reader:
                    date = line[0]
                    dt = date.split('-')
                    try:
                        price_datas[ticker][date] = {
                                                'TradeDate': datetime.datetime(*list(map(int, dt))).date(),
                                                'OpenPrice': round(float(line[1]), 2),
                                                'HighPrice': round(float(line[2]), 2),
                                                'LowPrice': round(float(line[3]), 2),
                                                'AdjClosePrice': round(float(line[5]), 2),
                                                'Volume': int(line[6]),       
                                            }        
                    except ValueError:
                        continue
    
    datas = {}
    process_file(file_path, datas)

    return datas

def main():
    share_prices = price_data('archive/stocks/*.csv')

    for k, v in share_prices.items():
        for item in v.values():
            print(tuple(item.values()))

if __name__ == '__main__':
    main()








