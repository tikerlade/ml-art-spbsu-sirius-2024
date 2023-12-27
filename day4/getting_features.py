import numpy as np
import pandas as pd
from skimage import color
from skimage.filters.rank import entropy
from skimage.morphology import disk
from PIL import Image
import os
import json


def CFN(img):
    pxls = color.rgb2lab(img[:, :, :3]).reshape([img.shape[0] * img.shape[1], 3])

    stda = np.std(pxls[:, 1])
    stdb = np.std(pxls[:, 2])

    centre = (
        np.sum(pxls[:, 1]) / pxls.shape[0],
        np.sum(pxls[:, 2]) / pxls.shape[0]
    )

    return int(np.hypot(stda, stdb) + 0.37 * np.hypot(centre[0], centre[1]))


def img_entropy(img):
    try:
        img = color.rgb2gray(img)
    except:
        img = color.rgba2gray(img)

    return entropy(img, disk(5))


def rgb_box_count(img, box_size):
    R, G, B = (img[:, :, i].flatten() for i in range(3))

    boxes = np.full((256 // box_size, 256 // box_size, 256 // box_size), False)

    for (r, g, b) in np.array([R, G, B]).T:
        boxes[
            int(r // box_size),
            int(g // box_size),
            int(b // box_size)
        ] = True

    return - np.log(np.sum(boxes)) / np.log(box_size / 256)


if __name__ == '__main__':
    df = pd.read_csv('images.csv')
    df = df.loc[df['Loaded']]
    print(len(df))
    if os.path.exists('tmp.json'):
        with open('tmp.json', 'r') as f:
            results = json.load(f)
    else:
        results = {}

    for _, row in df.iterrows():
        if row['image'] not in results:
            img = np.array(Image.open(f'Images\\{row["image"]}'))
            print(f'Processing {row["image"]}')
            results[row['image']] = {
                "cfn": CFN(img),
                "frac_dim": rgb_box_count(img, 2),
                "entr": np.mean(img_entropy(img)),
                "entr_std": np.std(img_entropy(img)),
                "price": row['normalized_price']
            }
            with open('tmp.json', 'w') as f:
                json.dump(results, f, indent=4)
        else:
            print('already there')
