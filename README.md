# API для Yatube
**RU**
## Описание
**API для проекта Yatube - это готовое решение готовое к взаимодействию с фронтендом блога Yatube, где у пользователей есть следующие возможности:**
>регистрация
>публикация постов
>публикация комментариев
>подписка на публикации прочих пользователей сервиса
## Установка

###Как запустить проект:

***Клонировать репозиторий и перейти в него в командной строке:***

git clone 
cd kittygram
Cоздать и активировать виртуальное окружение:
```
git clone git@github.com:your_username_in_github/api_final_yatube.git
python -m venv env
source venv/Script/activate
```
***Установить зависимости из файла requirements.txt:***

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

***Выполнить миграции:***

```
python manage.py migrate
```

***Запустить проект:***

```
python manage.py runserver
```

## Примеры
