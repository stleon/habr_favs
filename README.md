# habr_favs

## Установка

```
pyvenv-3.5 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Запуск

Принцип работы очень простой:

Парсим метки у статей, которые пользователь добавил в **избранное** на [Habrahabr](https://habrahabr.ru/) и [Geektimes](https://geektimes.ru/)

```
scrapy crawl favs -o tags.csv -s HABR_USER=lol
```

Где **lol** - логин пользователя. По-умолчанию, используется мой.

В файле **tags.csv** будут находится все метки этих статей.

Далее строим **word_cloud**:

```
python main.py
```

В итоге увидим файл **test.png** примерно такого содержания:

![Mine word_cloud](/test.png)