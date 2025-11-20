from .ticker_data_parser import stock_data

def reformat(data, type):
    '''Return Newly Formatted Data'''

    # return list[tuple(str, str, str, str | None, bool)]
    if type == 1: 
        
        return [tuple(stock_info.values()) for stock_info in data.values()]
    
    if type == 2:
        pass

    if type == 3:
        pass
    



def main():
    x = stock_data()
    y = reformat(x, 1)
    j = 0
    
    for vals in y:
        print(vals)
        if j == 3:
            break
        j+=1


if __name__ == "__main__":
    main()