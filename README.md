# ИИ раскрывает искусство: как машинное обучение помогает находить неизвестные закономерности на арт-рынке
В этом репозитории будут находиться задания для зимней школы СПбГУ для 11-классников, которая будет проходить в Сириусе с 9 по 24 января 2024 года.

## Практические задания
Занятия будут проходить после лекций, в формате 45 минут.

### 1. Знакомство с Orange
[Orange](https://orangedatamining.com/) - инструмент для анализа данных "no code" (т.е. код писать не надо, а результат анализа будет ничуть не хуже, чем используя код на Python).
На этом занятии мы посмотрим как:
* визуализировать входные данные;
* собирать описательные статистики по: текстам, картинкам, табличным данным;
* связывать между собой шаги обработки данных;

<img width="1374" alt="Screen Shot 2023-12-20 at 10 30 03" src="https://github.com/tikerlade/spbsu-sirius-2024/assets/28840497/6daa33b4-affb-4c22-bb55-9b1c5d538813">

#### Шаги на практике
1. Установка Orange;
2. Загрузка данных (Кубик загрузки данных);
3. Общая информация о наших данных (Data Info);
5. Отличия кубиков Data Info и Rank;
6. Выкинуть бесполезные колонки (выделить строчки, которые надо оставить в Data Info);
11. Кубик Pure Domain (удалить колонки, где уникальных значений = 1);
7. Найти колонки, где уникальных значений = 1 (Rank);
8. Для каких данных считается количество уникальных значений? (не для вещественных);
9. Кубик Feature Statistics (найти колонки, в которых есть пропуски);
12. Заполнить данные с пропусками кубиком Impute;
10. *Найти такие колонки, которые несут один и тот же смысл (коллинеарные);*
13. *Выкинуть коллинеарные колонки;*
14. Визуализация: Violin Plot, Scatter Plot, Box Plot;
15. Почему мы не можем впихнуть наши данные в Tree Plot?
16. Простейшая модель, типа Линейной регрессии
17. Анализ текстовых данных: 

#### Ссылки
* [Установка + Туториал по текстовым данным](https://hcommons.org/app/uploads/sites/1001924/2020/07/intro-to-orange-tutorial-part-1.pdf)

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

### 4. Предсказание цены по картине
В предсказании цены картины важны не только атрибуты связанные с ее автором / историей. Но и сама картина, ее качество влияют на стоимость самым непосредственным обрзаом. Поэтому в 4й день мы займемся тем, что обучим модель, которая будет предсказывать стоимость картины, основываясь на изображении.
Одним из входных признаков для модели будет выход модели, обученной днем ранее - стиль, в котором написана картина.

**TODO** - подготовить несколько Python функций, которые будут брать на вход картинку, а выдавать число /  вектор, которые можно будет использовать как признаки, чтобы школьникам самим не пришлось писать сложный код, связанный с нейронными сетями.

### 5. Генерация самой дорогой картины
Воспользуемся Шедеврумом, попробуем модели, доступные через Hugging Face, и попробуем сгенерировать шедевр, который будет стоить самых больших денег! Оценку стоимости будем производить моделью, обученной днем ранее.
* [Шедеврум](https://shedevrum.ai/) - можно генерировать картинки по описанию, и без использования кода;
* [Text-To-Image HuggingFace](https://huggingface.co/models?pipeline_tag=text-to-image&sort=trending) - генерировать картинки по тексту можно с помощью Python, так гораздо быстрее можно перебрать несколько параметров.

## Информация
**Лектор**: Дмитрий Алексеевич Григорьев

**Ассистент**: Кузнецов Иван
