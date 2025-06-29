# 🐶📈 Predict-Doge

A machine-learning project to analyze and forecast Dogecoin (DOGE) prices using historical market data and enriched feature sets.

---

## 📈 Model Results

We trained and evaluated four regression models on the historical Dogecoin dataset using a 70/30 chronological split with 1-day lag-based features (`market_cap`, `volume`, `volume_DOGE`, `open`, `high`, `low`).

### 🔍 Evaluation & Latest Prediction (as of 2025-06-28)

| Model              | MSE         | R² Score | Predicted Price (USD) |
|-------------------|-------------|----------|------------------------|
| Linear Regression | 0.000101    | 0.9842   | $0.157493              |
| Random Forest     | 0.000813    | 0.8733   | $0.162845              |
| XGBoost           | 0.001726    | 0.7311   | $0.164886              |
| LightGBM          | 0.000670    | 0.8956   | $0.167169              |

> 📊 See [`predict.ipynb`](./predict.ipynb) for training details, evaluation, and code.

### 📊 Actual vs. Predicted Price

<img src="./result_img/pred.png" alt="Prediction Comparison" width="800"/>

📘 **Notebook**: Full model training, evaluation metrics in [`predict_OHLCVM.ipynb`](./predict_OHLCVM.ipynb).
---

## 🚀 Project Status


| Component                            | Status            | Description                                                                |
|-------------------------------------|-------------------|----------------------------------------------------------------------------|
| **Data Collection**                  | 🔄 In Progress       | Full 2013–2025 dataset + automated daily updates (last 365 days)           |
| **Data Cleaning & EDA**              | ✅ Completed       | Removed anomalies, handled missing values, visualized trends with Plotly    |
| **Feature Engineering**              | 🔄 In Progress     | Added 1-day lags (`market_cap_lag1`, `volume_lag1`), rolling averages (7d)  |
| **Advanced Model Prototyping**       | 🔄 In Progress     | Testing Random Forest, XGBoost, and ARIMA                                  |

---

## 🔮 Future Plans

1. **Model Expansion**   
   - Explore **ARIMA**, **Prophet**, and **LSTM** for time-series forecasting.

2. **Enhanced Feature Sets**  
   - Add **multi-lag features** (e.g., 7-day and 30-day lags).  
   - Incorporate **technical indicators** (RSI, MACD) and **sentiment signals** from news/Twitter.

3. **Robust Validation**  
   - Apply **walk-forward cross-validation** to better estimate out-of-sample performance.  
   - Use **backtesting** on historical events (e.g., Elon Musk tweets).

4. **Deployment & Dashboarding**  
   - Build a lightweight **Streamlit** or **Dash** app to visualize live predictions.  
   - Automate daily data fetch and model retraining via GitHub Actions.

5. **Database Enrichment**  
   - Integrate **on-chain metrics** (e.g., transaction volume) and **exchange order-book data**.  
   - Store in a **PostgreSQL** or **MongoDB** backend for scalability.

---

⭐ If you find this project useful, please give it a star!  
