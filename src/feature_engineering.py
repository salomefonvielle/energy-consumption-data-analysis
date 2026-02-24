import pandas as pd
import numpy as np 

def add_datetime_features(df, date_col="date", drop_original=False):
    """
    Add year, month, day and time columns from a datetime column.

    Parameters:
        df (pd.DataFrame)
        date_col (str): name of the datetime column
        drop_original (bool): drop original date column or not

    Returns:
        pd.DataFrame
    """

    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])

    df["year"] = df[date_col].dt.year
    df["month"] = df[date_col].dt.month
    df["day"] = df[date_col].dt.day
    df["time"] = df[date_col].dt.time

    if drop_original:
        df = df.drop(columns=[date_col])

    return df


def add_holiday_feature(df, holidays, date_col="date"):
    """
    Add a binary 'is_holiday' column based on a list of (year, month, day) tuples.
    """

    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col]).dt.date

    holiday_dates = {
        pd.Timestamp(year=y, month=m, day=d).date()
        for (y, m, d) in holidays
    }

    df["is_holiday"] = df[date_col].isin(holiday_dates).astype(int)

    return df


def add_cyclical_time_features(df, date_col="date", drop_original=True):
    """
    Add cyclical time features (month, hour, day_of_week) using sine/cosine encoding.
    """

    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])

    # Basic time features
    df["day_of_week"] = df[date_col].dt.dayofweek
    df["hour"] = df[date_col].dt.hour
    df["month"] = df[date_col].dt.month

    # Cyclical encoding
    df["month_sin"] = np.sin(2 * np.pi * df["month"] / 12)
    df["month_cos"] = np.cos(2 * np.pi * df["month"] / 12)

    df["hour_sin"] = np.sin(2 * np.pi * df["hour"] / 24)
    df["hour_cos"] = np.cos(2 * np.pi * df["hour"] / 24)

    df["day_of_week_sin"] = np.sin(2 * np.pi * df["day_of_week"] / 7)
    df["day_of_week_cos"] = np.cos(2 * np.pi * df["day_of_week"] / 7)

    if drop_original:
        df = df.drop(
            columns=[
                "hour",
                "day_of_week",
                "month",
                "year",
                "day",
                "time",
                date_col
            ],
            errors="ignore"
        )

    return df