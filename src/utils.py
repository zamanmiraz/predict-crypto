def calculate_rsi(data, window=14):
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_macd(df, short_window=12, long_window=26, signal_window=9):
    df['EMA_short'] = df['weighted_price_box'].ewm(span=short_window, adjust=False).mean()
    df['EMA_long'] = df['weighted_price_box'].ewm(span=long_window, adjust=False).mean()
    df['MACD'] = df['EMA_short'] - df['EMA_long']
    df['Signal_Line'] = df['MACD'].ewm(span=signal_window, adjust=False).mean()
    return df

# Additional utility functions can be added here as needed.
# Calculate MVRV
def calculate_mvrv(df, market_cap, realized_cap):
    # compute the market cap
    
    return market_cap / realized_cap