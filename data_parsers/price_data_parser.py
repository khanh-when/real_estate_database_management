import csv
import glob
# from icecream import ic as print
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

                ticker = file.split('/')[-1].strip('.csv').replace('#', '.V') # parse for filename
                price_datas[ticker] = {}

                scale_100x = 0
                scale_1000x = 0
                rows = 0

                for line in csv_reader:
                    date = line[0]
                    dt = datetime.datetime(*list(map(int, date.split('-')))).date()

                    try:
                        # accept data entries from *2000 and later**
                        if dt < datetime.datetime(2000, 1, 1).date():
                            continue

                        # limit stock price range
                        if float(line[5]) > 1200:
                            continue

                        price_datas[ticker][date] = {
                                                'TradeDate': dt,
                                                'OpenPrice': round(float(line[1]), 2),
                                                'HighPrice': round(float(line[2]), 2),
                                                'LowPrice': round(float(line[3]), 2),
                                                'AdjClosePrice': round(float(line[5]), 2),
                                                'Volume': int(line[6]),       
                                            }
                        
                        # check if there is a scallar multiplier for volume
                        if int(line[6]) > 0:
                            scale_100x += 1 if (int(line[6]) % 100 == 0) else 0
                            scale_1000x += 1 if (int(line[6]) % 1000 == 0) else 0
                            rows+=1

                    except ValueError:
                        continue

                    print(f'rows: {rows} | scal100x: {scale_100x} | scal1000x: {scale_1000x}')

                if rows:   

                    if (scale_1000x/rows)*100 >= 90:     
                        for k in price_datas[ticker]:
                            price_datas[ticker][k]['Volume'] = int(price_datas[ticker][k]['Volume'] * 1000)
                    
                    # Real volume = CSV volume × 100, 
                    if (scale_100x / rows)*100 >= 90:     
                        for k in price_datas[ticker]:
                            price_datas[ticker][k]['Volume'] = int(price_datas[ticker][k]['Volume'] * 100)



                rows = 0

    
    datas = {}
    process_file(file_path, datas)

    return datas

def main():
    share_prices = price_data('archive/stocks/AAL.csv')

    # for k1, v in share_prices.items():
    #     for k2 in v:
    #         if k1 == 'A':
    #             print(k1, k2, share_prices[k1][k2]['Volume'])
    #         else:
    #             break

        # k1 = 'AAPL' key
        # share_prices[k] = ''
        # v = '2010-10-30': {rest data}
        # k2 = '2010-10-30' 

if __name__ == '__main__':
    main()



