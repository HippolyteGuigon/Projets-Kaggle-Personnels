import pandas as pd
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression


def _encode_dates(X):
    # Make sure that DateOfDeparture is of dtype datetime
    X = X.copy()  # modify a copy of X
    X.loc[:, "Date"] = pd.to_datetime(X['Date'])
    # Encode the date information from the DateOfDeparture columns
    X.loc[:, 'year'] = X['Date'].dt.year
    X.loc[:, 'month'] = X['Date'].dt.month
    X.loc[:, 'day'] = X['Date'].dt.day
    X.loc[:, 'weekday'] = X['Date'].dt.weekday
    X.loc[:, 'week'] = X['Date'].dt.week
    X.loc[:, 'n_days'] = X['Date'].apply(
        lambda date: (date - pd.to_datetime("1970-01-01")).days
    )
    # Finally we can drop the original columns from the dataframe
    return X.drop(columns=["Date"])


def get_estimator():
    date_encoder = FunctionTransformer(_encode_dates)

    categorical_encoder = OneHotEncoder(handle_unknown="ignore")
    categorical_cols = [
        "Arrival", "Departure", "year", "month", "day",
        "weekday", "week", "n_days"
    ]

    numerical_scaler = StandardScaler()
    numerical_cols = ["WeeksToDeparture", "std_wtd"]

    preprocessor = make_column_transformer(
        (categorical_encoder, categorical_cols),
        (numerical_scaler, numerical_cols)
    )

    regressor = LinearRegression()

    return make_pipeline(date_encoder, preprocessor, regressor)
