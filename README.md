# habr_favs

## Установка

```
git clone https://github.com/stleon/habr_favs.git
cd habr_favs
python3.7 -m venv venv
source venv/bin/activate
# for MAC OS
# export MACOSX_DEPLOYMENT_TARGET=10.15
pip install -r requirements.txt
```

## Запуск

Принцип работы очень простой:

Парсим метки у статей, которые пользователь добавил в **избранное** на [Habrahabr](https://habrahabr.ru/)

```
scrapy crawl favs -o tags.csv -s HABR_USER=lol
```

Где **lol** - логин пользователя. По-умолчанию, используется мой.

В файле **tags.csv** будут находится все метки этих статей.

```
cat tags.csv | tr '[:upper:]' '[:lower:]' | sort | uniq
```

Далее строим **word_cloud**:

```
python main.py
```

В итоге увидим файл **test.png** примерно такого содержания:

![Mine word_cloud](/test.png)