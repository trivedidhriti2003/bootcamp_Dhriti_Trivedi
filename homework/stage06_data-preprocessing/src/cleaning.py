# src/cleaning.py

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def fill_missing_median(df, columns):
    """
    Fills missing values in specified columns of a DataFrame with the median.

    Why median? The median is less sensitive to outliers (extremely high or
    low values) compared to the mean, making it a safer choice for filling
    missing data.

    Args:
        df (pd.DataFrame): The input DataFrame.
        columns (list): A list of column names to fill.

    Returns:
        pd.DataFrame: The DataFrame with missing values filled.
    """
    # Create a copy to avoid changing the original DataFrame
    df_cleaned = df.copy()
    for col in columns:
        # Calculate the median for the column
        median_val = df_cleaned[col].median()
        # Fill missing values (NaN) with the calculated median
        df_cleaned[col].fillna(median_val, inplace=True)
    print(f"Filled missing values in columns: {columns} using the median.")
    return df_cleaned


def drop_missing(df, threshold=0.5):
    """
    Drops columns with a high percentage of missing values.

    Why drop? If a column is mostly empty (e.g., 50% missing values), it
    often doesn't contain enough information to be useful and can be safely removed.

    Args:
        df (pd.DataFrame): The input DataFrame.
        threshold (float): The threshold of missing values to drop a column.
                           (e.g., 0.5 means drop if 50% or more is missing).

    Returns:
        pd.DataFrame: The DataFrame with sparse columns removed.
    """
    # Create a copy
    df_cleaned = df.copy()
    # Calculate the percentage of missing values for each column
    missing_percentage = df_cleaned.isnull().mean()
    # Get a list of columns to drop
    cols_to_drop = missing_percentage[missing_percentage > threshold].index
    # Drop the columns
    df_cleaned.drop(columns=cols_to_drop, inplace=True)
    if not cols_to_drop.empty:
        print(f"Dropped columns with more than {threshold*100}% missing values: {list(cols_to_drop)}")
    else:
        print("No columns exceeded the missing value threshold.")
    return df_cleaned


def normalize_data(df, columns):
    """
    Normalizes specified numerical columns to a range between 0 and 1.

    Why normalize? Many machine learning algorithms perform better when numerical
    features are on a similar scale. Normalization prevents features with large
    values (like 'Salary') from dominating features with small values (like 'Years_Experience').
    
    The formula used is Min-Max Scaling:
    $$ X_{\text{scaled}} = \frac{X - X_{\text{min}}}{X_{\text{max}} - X_{\text{min}}} $$

    Args:
        df (pd.DataFrame): The input DataFrame.
        columns (list): A list of numerical column names to normalize.

    Returns:
        pd.DataFrame: The DataFrame with normalized columns.
    """
    # Create a copy
    df_cleaned = df.copy()
    # Initialize the scaler
    scaler = MinMaxScaler()
    # Fit the scaler to the data and transform it
    df_cleaned[columns] = scaler.fit_transform(df_cleaned[columns])
    print(f"Normalized columns: {columns}")
    return df_cleaned