from data_loader.loader import DataLoader


def l1_error(origin, repaired):
    diff_df = repaired - origin
    abs_df = abs(diff_df)
    l1 = abs_df.sum().sum() / (abs_df.shape[0] * abs_df.shape[1])
    return l1


if __name__ == '__main__':
    df1 = DataLoader('oil', '01M00000000635561').load()
    df2 = df1 - 1.0
    print(l1_error(df1, df2))
