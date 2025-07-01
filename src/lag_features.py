import pandas as pd
import numpy as np


# create lag features n 
def create_lag_features(n, split=0.7):
    # --- Step 1: Load & Sort Data ---
    df = pd.read_csv('Dataset/doge_dataset_day_ohlcvm.csv', parse_dates=['date'])
    df = df.sort_values('date')
    df.dropna(inplace=True)
    df = df.copy()
    
    df[f'market_cap_lag{n}'] = df['market_cap'].shift(n)
    df[f'volume_lag{n}'] = df['volume'].shift(n)
    df[f'volume_DOGE_lag{n}'] = df['volume_DOGE'].shift(n)
    df[f'open_lag{n}'] = df['open'].shift(n)
    df[f'high_lag{n}'] = df['high'].shift(n)
    df[f'low_lag{n}'] = df['low'].shift(n)

    df.dropna(inplace=True)

    features = [
        f'market_cap_lag{n}',
        f'volume_lag{n}',
        f'volume_DOGE_lag{n}',
        f'open_lag{n}',
        f'high_lag{n}',
        f'low_lag{n}'
    ]
    target = 'close'

    X = df[features]
    y = df[target]

    # Chronological Train-Test Split
    train_size = int(len(df) * split)
    X_train, X_test = X.iloc[:train_size], X.iloc[train_size:]
    y_train, y_test = y.iloc[:train_size], y.iloc[train_size:]

    return X_train, X_test, y_train, y_test

