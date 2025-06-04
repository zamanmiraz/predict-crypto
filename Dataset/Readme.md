# 📊 Dataset Description

## Dogecoin 10 Years.json

**Source**: [Dogecoin 10 Years.json from Kaggle](https://www.kaggle.com/datasets/danieltsai04/dogecoin-historical-data-2013-2023/data)  
**API Reference**: [CoinGecko Public API](https://www.coingecko.com/api/documentation)

This dataset provides approximately 10 years of historical data on Dogecoin (DOGE) in USD, collected via the CoinGecko public API. It includes the following key metrics:

- **Price**
- **Market Capitalization**
- **24-Hour Trading Volume**

The data is originally provided in JSON format, structured as nested lists containing UNIX timestamps and their corresponding values. For example:
```json
"prices": [[timestamp, price], ...]
