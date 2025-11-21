from .stock_data_parser import stock_data

def reformat(data, type):
    '''Return Newly Formatted Data'''

    # return list[tuple(str, str, str, str | None, bool)]
    if type == 1: 
        return [tuple(stock_info.values()) for stock_info in data.values()]
    
    # return list[tuple(str, datetime, float, float, float, float, int))]
    if type == 2:
        return [(k, *share_data.values()) for k, v in data.items() for share_data in v.values()]

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