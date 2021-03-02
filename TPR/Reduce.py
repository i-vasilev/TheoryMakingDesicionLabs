def reduce(matrix):
    for index_, row in matrix.iterrows():
        for index, row1 in matrix.iterrows():
            if row > row1 & index != index_:
                matrix.drop(index_, inplace=True)
    print(1)
    pass
