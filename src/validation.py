import pandas as pd 

def split_data(X, n=0):
    """
    Validation glissante en 5 blocs.
    n ∈ {0,1,2,3,4}
    """
    train_percentage = 0.8

    if n == 0:
        train_size = int(train_percentage * len(X))
        return X[:train_size], X[train_size:]

    else:
        test_percentage = 1 - train_percentage
        div1 = int((train_percentage - n * test_percentage) * len(X))
        div2 = int((train_percentage - (n - 1) * test_percentage) * len(X))

        return (
            pd.concat([X[:div1], X[div2:]]),
            X[div1:div2]
        )
