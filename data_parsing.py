
ticker_data = {}

with open('archive/symbols_valid_meta.csv') as f:

    line = f.readline().split(',')

    ticker_data[line[1]] = [] # securities
    ticker_data[line[2]] = [] # s_name
    ticker_data[line[3]] = [] # Listing
    ticker_data[line[4]] = [] # Market Category
    ticker_data[line[5]] = [] # ETF

    print('\n',line)

    print('\n',f.readline())

    print('\n', ticker_data)
