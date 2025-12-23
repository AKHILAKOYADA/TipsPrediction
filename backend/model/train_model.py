import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib


def train_model(df):
    """Train a machine learning model using the provided dataframe."""

    # separate features and target variable
    x = df.drop("tip", axis=1)
    y = df["tip"]

    # identify categorical and numerical columns
    categorical_cols = x.select_dtypes(include=["object", "category"]).columns
    numerical_cols = x.select_dtypes(exclude=["object", "category"]).columns

    # create preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", "passthrough", numerical_cols),
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ]
    )

    # create a pipeline with preprocessor and model
    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", RandomForestRegressor(random_state=42)),
        ]
    )

    # split the data
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    # train the model
    model.fit(x_train, y_train)

    return model
