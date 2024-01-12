import Orange, pickle
import math

from orangecontrib.imageanalytics.image_embedder import ImageEmbedder

def get_embedding(img_path):
    with ImageEmbedder(model='painters') as emb:
        emb.clear_cache()
        return emb([img_path])

def get_style_prediction(img_path):
    emb = get_embedding(img_path)

    # Можно еще научиться выводить уверенность предсказания (оценки вероятностей)
    model = pickle.load(open('style_classifier.pkcls', 'rb'))
    style = model(emb)

    return [model.domain.class_var.str_val(i) for i in style]

def get_price_prediction(img_path):
    emb = get_embedding(img_path)

    model = pickle.load(open('price_predictor.pkcls', 'rb'))
    pred_log_price = model(emb)
    price = math.e ** pred_log_price

    return price

# img_path = './052n10381-bdw3h-a.jpg'
img_path = './example.jpg'
print(get_embedding(img_path))
print('Style: ', get_style_prediction(img_path))
print('Price: ', get_price_prediction(img_path))