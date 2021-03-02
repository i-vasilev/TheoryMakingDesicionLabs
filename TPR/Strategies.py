from pandas import array


class Strategies:
    @staticmethod
    def solveInClearStrategies(matrix):
        minimax = matrix.min(axis=1).max()
        maximin = matrix.max().min()
        if minimax == maximin:
            return [matrix.min(axis=1).idxmax(), matrix.max().idxmin(axis=0)]
        return None

    @staticmethod
    def solveInMixedStrategies(matrix):
        pass
