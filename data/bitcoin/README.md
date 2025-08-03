# Bitcoin Historical Data

This folder contains the daily historical price and volume data for Bitcoin (BTC) sourced from the [Kaggle “Bitcoin Historical Data” dataset](https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data) by Michał C. Zieliński.

> **Dataset summary:**  
> - **Date range:** January 1, 2010 – present  
> - **Frequency:** Daily  
> - **Records:** ~3,000+ days of trading data  

## 📊 Columns

| Column            | Description                                                |
|-------------------|------------------------------------------------------------|
| `Timestamp`       | UTC Timestamp                                              |
| `Open`            | Opening price at start of day                              |
| `High`            | Highest price during the day                               |
| `Low`             | Lowest price during the day                                |
| `Close`           | Closing price at end of day                                |
| `Volume_(BTC)`    | Volume traded in BTC                                       |

## 📅 Updating the Dataset

To refresh the Bitcoin dataset with the latest data, run the script located at: `../src/update_bitcoin.py`
 
> **Source credit:**  
> Zieliński, M. C. “Bitcoin Historical Data.” Kaggle, 2018.  
> URL: https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data  
