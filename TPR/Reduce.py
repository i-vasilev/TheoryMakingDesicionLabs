import pandas as pd


def reduce(df):
    while True:
        size = df.size
        df = reduce_by_cols(df)
        df = reduce_by_rows(df)
        if size == df.size:
            break
    return df


def is_row_larger_than_other(row1, row2):
    for index_, row1_ in row1.items():
        if row1[index_] < row2[index_]:
            return False
    return True


def reduce_by_rows(df):
    for index_, row in df.iterrows():
        for index, row1 in df.iterrows():
            if is_row_larger_than_other(row, row1) & (index != index_) & (index_ in df.index):
                df.drop(index_, inplace=True)
    return df


def reduce_by_cols(df):
    s = pd.Series()
    for index_, row in df.iteritems():
        for index, row1 in df.iteritems():
            if is_row_larger_than_other(row, row1) & (index != index_) & (index_ in df):
                s["index_"] = index_
    df.drop(s, axis=1, inplace=True)
    return df
