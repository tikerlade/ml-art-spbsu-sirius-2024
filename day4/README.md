# День 4. Предсказание цены по картине
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1xXDgiXnyrp6rgYiDLISNmelksSbr4HBV?usp=sharing)

В предсказании цены картины важны не только атрибуты связанные с ее автором / историей. Но и сама картина, ее качество влияют на стоимость самым непосредственным обрзаом. Поэтому в 4й день мы займемся тем, что обучим модель, которая будет предсказывать стоимость картины, основываясь на изображении и признаках эстетичности.
Одним из входных признаков для модели будет выход модели, обученной днем ранее - стиль, в котором написана картина.

## Наши наполеоновские планы на день
1. Решаем задачу регрессии цены на голых эмбеддингах
2. Добавляем признак - стиль картины, предсказанный вчерашней моделью
3. Рассчитываем 4 признака - метрики эстетичности 
4. Добавляем в наш датасет 4 новых признака и строим регрессию на этих признаках
5. Экспорт модели и использование ее в Python скрипте

## Домашнее задание
Дописать подсчет метрики эстетичности `METRIC`, обучить модели, посмотреть, что стало лучше.

## Статьи
Ссылки на статьи, рассмотренные на лекции:
* [History of art paintings through the lens of entropy and complexity](https://www.pnas.org/doi/full/10.1073/pnas.1800083115)
* [Measuring colourfulness in natural images (pdf)](https://infoscience.epfl.ch/record/33994/files/HaslerS03.pdf)
* [Computational aesthetics and applications (pdf)](https://www.researchgate.net/publication/327447399_Computational_aesthetics_and_applications/fulltext/5b900d0aa6fdcc327e4586dd/Computational-aesthetics-and-applications.pdf?origin=publicationDetail&_sg%5B0%5D=mfaLMeGqdqOC52idfEvvnlspEPtGJ-uxuO6ljpZKm5wULsEND8S2upR3njgy9FFFsJHvdpBZxwu9Mv0sRuL8kA.ZN423jc5gOmJSm15_QMbbo6yGFika_6sO1wo4rmF1X1ljL2c75HkKVg-cqXgTmHPcr9-UZZ4btx-EUSy_C8BKQ&_sg%5B1%5D=frr6J38fvL68b9aiHCcvimomQIb6Z_Kx-Rajy-HUIFeZj9iws_WtNyKnj-r-HYVBHQTjuBWV18WvuBlKQeC67LN0MWSPvuPGdX8DLrWAm75V.ZN423jc5gOmJSm15_QMbbo6yGFika_6sO1wo4rmF1X1ljL2c75HkKVg-cqXgTmHPcr9-UZZ4btx-EUSy_C8BKQ&_iepl=&_rtd=eyJjb250ZW50SW50ZW50IjoibWFpbkl0ZW0ifQ%3D%3D&_tp=eyJjb250ZXh0Ijp7ImZpcnN0UGFnZSI6InB1YmxpY2F0aW9uIiwicGFnZSI6InB1YmxpY2F0aW9uIiwicG9zaXRpb24iOiJwYWdlSGVhZGVyIn19)
* [Inkthetics: A Comprehensive Computational Model for Aesthetic Evaluation of Chinese Ink Paintings](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9293299)