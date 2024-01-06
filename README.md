![logo](https://github.com/tikerlade/spbsu-sirius-2024/assets/28840497/4f35ab40-371b-48b1-a0a9-7a5a77708a8f)

В этом репозитории будут находиться задания для зимней школы СПбГУ для 11-классников, которая будет проходить в Сириусе с 9 по 13 января 2024 года.

### Практические задания
Занятия будут проходить после лекций, в формате 45 минут. Темы занятий будут следующие:
1. EDA: Описательные статистики
2. Feature Engineering + Basic ML
3. В каком стиле написана картина
4. Определяем стоимость по изображению картины
5. Генерируем шедевры

### Используемые инструменты
На занятиях мы будем использовать разные инструменты:
* [Orange](https://orangedatamining.com/) - инструмент для анализа данных "no code";
* [HuggingFace API](https://huggingface.co/docs/api-inference/quicktour) -  огромная библиотека различных моделей машинного обучения;

### Примеры результатов
Один из пайплайнов построенных в Orange

<img width="600" alt="Screen Shot 2023-12-20 at 10 30 03" src="https://github.com/tikerlade/spbsu-sirius-2024/assets/28840497/6daa33b4-affb-4c22-bb55-9b1c5d538813">


### Авторы курса
**Лектор**: Дмитрий Алексеевич Григорьев
**Ассистент**: Кузнецов Иван


### Ссылки
* [Установка Orange + Туториал по текстовым данным](https://hcommons.org/app/uploads/sites/1001924/2020/07/intro-to-orange-tutorial-part-1.pdf)

---

### 2. Анализ цен с аукционов Sotheby’s и Christie’s
На аукционах товары довольно часто продаются по цене, которая превышает начальную. Один из предметов, которые часто продаются на аукционах - картины.
С помощью Orange мы посмотрим какие есть закономерности у дорогих картин, найдем самые важные признаки для того, чтобы картина стоила дорого:
* проведем Exploratory Data Analysis (EDA) - посмотрим как устроена природа входных данных;
* настроим процесс предсказания финальной цены основываясь на численных данных;
* добавим использование текстов для предсказания цены.

Используя модель, которую мы обучим надо будет попробовать предсказать наиболее перспективные лоты с предстоящих торгов.


* посмотрим как оценить результат нашей модели
* как посмотреть на сколько коллинеарность и вправду нам мешала
* какие методы для вставки пропусков помогают, а какие делают результат хуже
* что такое stacking? оценим результаты 


_В качестве данных будет использован датасет, предоставленный Д. А. Григорьевым._

### 3. В каком стиле написана картина?
У каждого художника свой стиль. И заядлые коллекционеры с легкостью отличат один стиль от другого. Посмотрим, способны ли на это алгоритмы машинного обучения: попробуем решить эту задачу с помощью Orange.

В качестве данных будем использовать картины из датасета по аукционам. Там лежат ссылки на картины. Следовательно картины можно скачать, а затем разметить моделями, которые были обучены на датасете Kaggle:  _"WikiArt Art Movements/Styles" [ссылка](https://www.kaggle.com/code/mpwolke/expressing-my-scream/input)_
**TODO** - подготовить разметку

* Можно рассказать про то, что такоей файнтюнинг, и показать скрипт подготовки данных (возможно с заданием)
  
**ДЗ: найти стиль с самой дорогой ценой.**

### 4. Предсказание цены по картине
В предсказании цены картины важны не только атрибуты связанные с ее автором / историей. Но и сама картина, ее качество влияют на стоимость самым непосредственным обрзаом. Поэтому в 4й день мы займемся тем, что обучим модель, которая будет предсказывать стоимость картины, основываясь на изображении.
Одним из входных признаков для модели будет выход модели, обученной днем ранее - стиль, в котором написана картина.

**TODO** - подготовить несколько Python функций, которые будут брать на вход картинку, а выдавать число /  вектор, которые можно будет использовать как признаки, чтобы школьникам самим не пришлось писать сложный код, связанный с нейронными сетями.

### 5. Генерация самой дорогой картины
Воспользуемся Шедеврумом, попробуем модели, доступные через Hugging Face, и попробуем сгенерировать шедевр, который будет стоить самых больших денег! Оценку стоимости будем производить моделью, обученной днем ранее.
* [Шедеврум](https://shedevrum.ai/) - можно генерировать картинки по описанию, и без использования кода;
* [Text-To-Image HuggingFace](https://huggingface.co/models?pipeline_tag=text-to-image&sort=trending) - генерировать картинки по тексту можно с помощью Python, так гораздо быстрее можно перебрать несколько параметров.

Будем исползьовать генеративные модели, которые доступны на HuggingFace через API, т.к. порой они требуют чересчур много ресурсов.

#### TODO
* Jupyter Notebook API inference;
* Jupyter Notebook Generative loop (10 epochs);
* Добавить чит-проверку, что в промпте не содержится явной оценки стоимости картины
* Эволюционный алгоритм: на каждой итерации добавляем 1 слово в предыдущий промпт и смотрим на сколько изменяется предсказание цены.


План:
* Рассказать про HuggingFace, почему полезен и зачем нужен
* Выдать ноутбук под GPT, в котором проставлены TODO для адаптации к картинкам


