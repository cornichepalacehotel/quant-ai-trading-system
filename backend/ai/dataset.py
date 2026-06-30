import pandas as pd

class Dataset:

    def prepare(self, df):

        df = df.copy()

        df = df.dropna()

        return df
