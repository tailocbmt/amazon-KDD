import os
import sys

sys.path.append('../')

import pandas as pd

from utils.process import clean_html, null_product_title

def main():
    query = pd.read_csv('../dataset/train-v0.2.csv')
    catalog = pd.read_csv('../dataset/product_catalogue-v0.2.csv')
    # Merge 2 dataframe
    merge = query.merge(catalog, how='left', left_on=['query_locale','product_id'], right_on=['product_locale', 'product_id'])

    # Null product_title
    merge = null_product_title(merge)
    print((merge.isnull().sum() / len(merge)) * 100)


    clean_cols = ['product_description', 'product_bullet_point']

    # Remove html tags
    for col in clean_cols:
        merge[col] = merge[col].apply(lambda x: clean_html(x))
    
    merge.to_csv('../dataset/train_product_catalogue-v0.2.csv', index=False)

if __name__ == "__main__":
    main()