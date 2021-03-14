import pandas as pd


def minimax(df):
    for index_row, row in df.iterrows():
        for index_column, column in row.iteritems():
            if row.min() == row[index_column] == df[index_column].max():
                return [index_row, index_column]
    return None


def minimax_strategies(df, vec):
    strategies = pd.DataFrame(columns=["i", "j"])
    for index_column, column in df.iteritems():
        if (df[vec[0]][vec[1]] == column.max() == df[index_column][vec[1]]) & (index_column > vec[0]):
            strategies.loc[len(strategies)] = [vec[0], index_column]
    return strategies


def maximin_strategies(df, vec):
    strategies = pd.DataFrame(columns=["i", "j"])
    for index_row, row in df.iterrows():
        if (df[vec[0]][vec[1]] == row.min() == df[vec[0]][index_row]) & (index_row > vec[1]):
            strategies.loc[len(strategies)] = [vec[1], index_row]
    return strategies

