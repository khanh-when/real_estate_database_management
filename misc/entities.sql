
-- Create Stock Entity Table
-- @block
CREATE TABLE Stocks(
    StockID VARCHAR(6) PRIMARY KEY,
    SecurityName VARCHAR(264),
    ListingExchange CHAR NULL,
    MarketCategory CHAR NULL,
    ETF BOOLEAN
);

-- @block
DROP TABLE Stocks;

-- Create Price_Data Entity Table
-- @block
CREATE TABLE PriceData(
    StockID VARCHAR(6),
    TradeDate DATE,
    OpenPrice Decimal(10, 2) UNSIGNED,
    HighPrice Decimal(10, 2) UNSIGNED,
    LowPrice DECIMAL(10, 2) UNSIGNED,
    AdjClosePrice DECIMAL(10, 2) UNSIGNED,
    Volume INT UNSIGNED,
    PRIMARY KEY(StockID, TradeDate),
    FOREIGN KEY (StockID) REFERENCES Stocks(StockID)
)

--  @block
DROP TABLE PriceData;
