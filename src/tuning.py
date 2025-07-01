from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.metrics import mean_squared_error, r2_score

def tune_random_forest(X_train, y_train, X_test, y_test):
    param_dist_rf = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'max_features': ['sqrt', 'log2', None] 
    }

    rf_random = RandomizedSearchCV(
        RandomForestRegressor(random_state=42),
        param_distributions=param_dist_rf,
        n_iter=20,
        cv=3,
        scoring='neg_mean_squared_error',
        random_state=42,
        n_jobs=-1
    )
    rf_random.fit(X_train, y_train)
    best_rf = rf_random.best_estimator_
    preds = best_rf.predict(X_test)
    return best_rf, mean_squared_error(y_test, preds), r2_score(y_test, preds)

def tune_xgboost(X_train, y_train, X_test, y_test):
    param_dist_xgb = {
        'n_estimators': [100, 200, 300],
        'max_depth': [3, 5, 7],
        'learning_rate': [0.01, 0.05, 0.1],
        'subsample': [0.6, 0.8, 1.0],
        'colsample_bytree': [0.6, 0.8, 1.0]
    }

    xgb_random = RandomizedSearchCV(
        XGBRegressor(random_state=42),
        param_distributions=param_dist_xgb,
        n_iter=20,
        cv=3,
        scoring='neg_mean_squared_error',
        random_state=42,
        n_jobs=-1
    )
    xgb_random.fit(X_train, y_train)
    best_xgb = xgb_random.best_estimator_
    preds = best_xgb.predict(X_test)
    return best_xgb, mean_squared_error(y_test, preds), r2_score(y_test, preds)

def tune_lightgbm(X_train, y_train, X_test, y_test):
    param_dist_lgb = {
        'n_estimators': [100, 200, 300],
        'learning_rate': [0.01, 0.05, 0.1],
        'max_depth': [3, 5, 7, -1],
        'num_leaves': [31, 50, 100],
        'subsample': [0.6, 0.8, 1.0],
        'colsample_bytree': [0.6, 0.8, 1.0]
    }

    lgb_random = RandomizedSearchCV(
        LGBMRegressor(random_state=42),
        param_distributions=param_dist_lgb,
        n_iter=20,
        cv=3,
        scoring='neg_mean_squared_error',
        random_state=42,
        n_jobs=-1
    )
    lgb_random.fit(X_train, y_train)
    best_lgb = lgb_random.best_estimator_
    preds = best_lgb.predict(X_test)
    return best_lgb, mean_squared_error(y_test, preds), r2_score(y_test, preds)
