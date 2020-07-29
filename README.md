# Wllpprs_v1

### Что ты такое?

Первая версия сервиса, предлагающего пользователю обои для рабочего стола по ключевому слову.

### Как запустить?

Склонируйте репозиторий:

```bash
https://github.com/sh4rpy/wllpprs_v1.git
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

Создайте файл .env в одной директории с файлом settings.py. Создайте в нем переменные окружения  SECRET_KEY и CLIENT_ID. Первой присвойте ключ, скопированный с [сайта генерация ключей](https://djecrety.ir), а второй присвойте access_key, который можно получить при регистрации на [unsplash](https://unsplash.com) как разработчик. Выглядеть файл должен так:

```python
SECRET_KEY=y%jti6sfm66#e0g^47=x961bvs%)c#t7&=2z)5dzz3a9py2x2&
CLIENT_ID=3iLImdZAPSLA-LHINaa_C3bQSFOP89hM0y5livdRq-bul4
```

Выполните миграции:

```bash
python manage.py migrate
```