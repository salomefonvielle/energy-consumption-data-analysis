def standardize_train_validation(train_df, val_df, cols_to_exclude=None):
    """
    Standardize train and validation sets using train statistics only.
    """

    train_df = train_df.copy()
    val_df = val_df.copy()

    if cols_to_exclude is None:
        cols_to_exclude = []

    cols_to_normalize = train_df.columns.difference(cols_to_exclude)

    means = train_df[cols_to_normalize].mean()
    stds = train_df[cols_to_normalize].std()

    train_df[cols_to_normalize] = (
        train_df[cols_to_normalize] - means
    ) / stds

    val_df[cols_to_normalize] = (
        val_df[cols_to_normalize] - means
    ) / stds

    return train_df, val_df
