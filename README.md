# 🐶 Predict-Doge

A machine-learning project to analyze and forecast Dogecoin (DOGE) prices using historical market data and enriched feature sets.

---

## 📈 Model Results

Four regression models were trained and evaluated on the historical Dogecoin dataset using a 70/30 chronological split. The models leveraged 1-day lag-based features (`market_cap`, `volume`, `volume_DOGE`, `open`, `high`, `low`). Hyperparameter tuning was also performed to optimize performance.

<!-- ### 🔍 Evaluation & Latest Prediction (as of 2025-06-28) -->

<!-- | Model              | MSE         | R² Score | Predicted Price (USD) |
|-------------------|-------------|----------|------------------------|
| Linear Regression | 0.000101    | 0.9842   | $0.157493              |
| Random Forest     | 0.000813    | 0.8733   | $0.163134              |
| XGBoost           | 0.001726    | 0.7311   | $0.169618             |
| LightGBM          | 0.000670    | 0.8956   | $0.161885              | -->

### 📊 Model Performance Across Lag Days

| Model              | 1-Day MSE | 1-Day R² | 2-Day MSE | 2-Day R² | 3-Day MSE | 3-Day R² | 4-Day MSE | 4-Day R² |
|-------------------|-----------|----------|-----------|----------|-----------|----------|-----------|----------|
| Linear Regression | 0.000101  | 0.9842   | 0.000186  | 0.9710   | 0.000273  | 0.9574   | 0.000372  | 0.9421   |
| Random Forest     | 0.000724  | 0.8873   | 0.001724  | 0.7313   | 0.003403  | 0.4703   | 0.005207  | 0.1894   |
| XGBoost           | 0.001445  | 0.7749   | 0.001115  | 0.8262   | 0.001804  | 0.7192   | 0.003077  | 0.5210   |
| LightGBM          | 0.000504  | 0.9215   | 0.000717  | 0.8884   | 0.001754  | 0.7269   | 0.003881  | 0.3959   |


📖 **Detailed Explanation**  
For an in-depth discussion of the results and model comparisons, check out the accompanying Medium article:  
👉 [When Simplicity Wins: Linear Regression Tops Complex Models in 1-Day Lag Dogecoin Forecasting](https://medium.com/@mirazzaman/when-simplicity-wins-linear-regression-tops-complex-models-in-1-day-lag-dogecoin-forecasting-4f7d1965e3a4)


> See [`predict.ipynb`](./predict.ipynb) for training details, evaluation, and code.

### 📊 Actual vs. Predicted Price (1-Day Lag)

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