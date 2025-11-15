stock = {}

def parse_csv(line: str):
    parsed_data = []
    inquote = False
    tok = ''

    for ch in line.split(','):

        if ch:
 
            if ch[0] == '"':
                inquote = True
                tok += ch
                continue

            if ch[-1] == '"' and inquote:
                tok += ch
                inquote = False
                ch = tok.strip('\"\'')

        parsed_data.append(ch)
        

    return parsed_data

with open('archive/symbols_valid_meta.csv') as f:
    line = f.readline() # skip header line

    line = f.readline()
    print('1.', line)
    print('1.', line.split())


    line = parse_csv(line)
    print('3.', line)

    

    # line = line.strip().split(',')

    # print('2.', line)

    # symbol = line[1]
    # stock[symbol] = {
    #     'Stock_ID': symbol,
    #     'SecurityName': line[2].strip('\"\' '),
    #     'ListingExchange': line[3].strip("\"\' "),
    #     'MarketCategory': line[4],
    #     'ETF': line[5]
    # }

    # print('3.',stock)

