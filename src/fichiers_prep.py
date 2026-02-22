import pandas as pd

def resample_and_interpolate(
    df,
    date_col="date",
    numeric_cols=None,
    freq="30min",
    interpolation_method="linear"
):
    """
    Convert date column, resample time series to a fixed frequency,
    and interpolate numeric columns.
    
    Parameters:
        df (pd.DataFrame): Input dataframe
        date_col (str): Name of the date column
        numeric_cols (list): Columns to convert and interpolate
        freq (str): Resampling frequency (e.g. '30min')
        interpolation_method (str): Interpolation method
    
    Returns:
        pd.DataFrame: Resampled and interpolated dataframe
    """

    df = df.copy()

    # Convert date column
    df[date_col] = pd.to_datetime(df[date_col])

    # Convert selected columns to numeric
    if numeric_cols is not None:
        df[numeric_cols] = df[numeric_cols].apply(
            pd.to_numeric, errors="coerce"
        )

    # Set date as index
    df.set_index(date_col, inplace=True)

    # Create new time index
    new_index = pd.date_range(
        start=df.index.min(),
        end=df.index.max(),
        freq=freq
    )

    # Reindex
    df = df.reindex(new_index)

    # Interpolate
    df = df.interpolate(method=interpolation_method)

    # Reset index
    df = df.reset_index().rename(columns={"index": date_col})

    return df


def merge_on_datetime(
    df1,
    df2,
    date_col_df1="time",
    date_col_df2="date",
    output_date_col="date",
    how="inner"
):
    """
    Rename, convert to datetime and merge two DataFrames on a date column.
    """

    df1 = df1.copy()
    df2 = df2.copy()

    # Rename column if necessary
    if date_col_df1 != output_date_col:
        df1.rename(columns={date_col_df1: output_date_col}, inplace=True)

    # Convert to datetime
    df1[output_date_col] = pd.to_datetime(df1[output_date_col])
    df2[date_col_df2] = pd.to_datetime(df2[date_col_df2])

    # Merge
    merged_df = pd.merge(
        df1,
        df2,
        left_on=output_date_col,
        right_on=date_col_df2,
        how=how
    )

    return merged_df

def filter_by_date_range(
    df,
    date_col="date",
    start_date=None,
    end_date=None
):
    """
    Filter dataframe between two dates.
    """

    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col])

    if start_date is not None:
        df = df[df[date_col] >= pd.to_datetime(start_date)]

    if end_date is not None:
        df = df[df[date_col] <= pd.to_datetime(end_date)]

    return df