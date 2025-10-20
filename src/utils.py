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

def add_technical_indicators(df):
    """
    Add common technical indicators to df (expects columns: Open, High, Low, Close, Volume).
    Requires 'ta' library (pip install ta) or adapt to pandas_ta.
    """
    import ta

    df = df.copy()
    # Momentum
    df['RSI_14'] = ta.momentum.RSIIndicator(df['Close'], window=14).rsi()
    # Trend
    macd = ta.trend.MACD(df['Close'])
    df['MACD'] = macd.macd()
    df['MACD_Signal'] = macd.macd_signal()
    df['EMA_20'] = ta.trend.EMAIndicator(df['Close'], window=20).ema_indicator()
    df['SMA_50'] = ta.trend.SMAIndicator(df['Close'], window=50).sma_indicator()
    # Volatility
    bb = ta.volatility.BollingerBands(df['Close'], window=20, window_dev=2)
    df['BB_H'] = bb.bollinger_hband()
    df['BB_L'] = bb.bollinger_lband()
    # Strength / Volume
    df['ADX_14'] = ta.trend.ADXIndicator(df['High'], df['Low'], df['Close'], window=14).adx()
    df['OBV'] = ta.volume.OnBalanceVolumeIndicator(df['Close'], df['Volume']).on_balance_volume()

    return df