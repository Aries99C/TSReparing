import pandas as pd


if __name__ == '__main__':
    oil_df = pd.read_csv('../dataset/oil/oil.csv')
    mId_list = oil_df['SBBM'].unique()
    data_list = []
    for mId in mId_list:
        data_list.append(
            (oil_df[oil_df['SBBM'] == mId].drop(
            columns=['SBBM', 'LINKEDPROVINCE', 'DYDJ', 'ACQUISITIONTIME']),
            mId)
        )
    for data_slice, mId in data_list:
        data_slice = data_slice.reset_index(drop=True)
        data_slice.to_csv('../dataset/oil/' + mId + '.csv')
