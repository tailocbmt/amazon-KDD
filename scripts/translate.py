import json

from easynmt import EasyNMT
import pandas as pd

def write_json(json_path, contents, encoding='utf8'):
    try:
        with open(json_path, 'w', encoding=encoding) as convert_file:
            json.dump(
                contents, convert_file, ensure_ascii=False)
    except:
        raise Exception('Error when writing file')

def main():
    df = pd.read_csv('dataset/product_catalogue-v0.2.csv')

    model = EasyNMT('opus-mt')

    language_vals = df['product_locale'].unique()

    for col in ['product_title', 'product_description', 'product_bullet_point','product_brand', 'product_color_name']:
        mapping = {}

        for lang in language_vals:
            if lang == 'us':
                continue
            df[col] = df[col].astype(str)
            unique_vals = df.loc[df['product_locale']==lang, col].unique()
            print(len(unique_vals))

            translations = model.translate(unique_vals, source_lang=lang ,target_lang='en', batch_size=60, show_progress_bar=True, beam_size=3)

            for i in range(len(translations)):
                mapping[unique_vals[i]] = translations[i]

        write_json(f'../drive/MyDrive/amazon-KDD/{col}_mapping.json', mapping)

if __name__ == "__main__":
    main()
