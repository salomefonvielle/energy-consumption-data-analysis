import pandas as pd

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