import re

import pandas as pd

# Remove HTML tags
def clean_html(raw_string):
    raw_string = str(raw_string)
    html_regex = r'<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});'
    pattern = re.compile(html_regex)
    cleaned_text = re.sub(pattern, '', raw_string)

    return cleaned_text

def null_product_title(df):
    replace_df = df.loc[pd.isna(df['product_title']) & df['esci_label']=='exact',:]
    for idx, row in replace_df.iterrows():
        df.at[idx, 'product_title'] = row['query']
    
    df = df.dropna(subset=['product_title'])
    return df