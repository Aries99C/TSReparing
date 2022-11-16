import pandas as pd


class DataLoader(object):
    def __init__(self, dataset, mId):
        self.dataset = dataset
        self.mId = mId
        self.df = pd.read_csv('../dataset/' + dataset + '/' + mId + '.csv', index_col=0)

    def load(self):
        return self.df


if __name__ == '__main__':
    test = DataLoader('oil', '01M00000000635561').load()
