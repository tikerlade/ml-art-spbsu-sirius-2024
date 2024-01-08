import pandas as pd
import requests
from requests.exceptions import Timeout, ConnectionError


def get_images(row: pd.Series) -> pd.Series:
    i = row['Image']
    print(f'{i}')
    try:
        r = requests.get(i, timeout=5)
    except (Timeout, ConnectionError) as e:
        row['Loaded'] = False
        print('Not')
    else:
        name = i.split('/')[-1]
        if name[-4:] != '.jpg':
            row['Loaded'] = False
            print('Bad')
        else:
            row['Loaded'] = True
            print(f'Got!')
            with open(f"Images_demo\\{i.split('/')[-1]}", "wb") as f:
                f.write(r.content)
                f.close()
            row['image'] = i.split('/')[-1]
    return row


df = pd.read_csv('./../new_data.csv')
df = df.loc[df['Image'] != '�']
df = df.loc[~df['Image'].isna()]

images = df['Image'].to_list()
df.apply(get_images, axis=1).reset_index()[['image', 'normalized_price', 'Loaded']].to_csv('./../images.csv')
