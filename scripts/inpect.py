import pandas as pd

df = pd.read_csv('../dataset/train-v0.2.csv')

print(df.tail(10))

df_p = pd.read_csv('../dataset/product_catalogue-v0.2.csv')

df = df.merge(df_p, on='product_id', how='right')
print(df_p.tail(10))

print(df.loc[df['esci_label']=='exact', :])