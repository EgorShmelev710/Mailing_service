﻿# Mailing_service

## Описание

Это сервис рассылок Mailings. С его помощью можно создавать
рассылки, которые сервис будет автоматически отправлять заданным клиентам в заданное время!

## Технологии

- Python
- Django
- PostgreSQL
- Redis

## Настройка проекта

### Клонирование проекта

Для работы с проектом клонируйте репозиторий

  ```sh
  git clone git@github.com:EgorShmelev710/Course_work_6.git
  ```

### Настройка виртуального окружения

Создайте виртуальное окружение командой:

```text
python3 -m venv venv
```

Активируйте виртуальное окружение:

```text
source venv/bin/activate          # для Linux и Mac
venv\Scripts\activate.bat         # для Windows
```

Устанавите зависимости командой:

```text
pip install -r requirements.txt
```

### Редактирование .env.sample:

- В корне проекта переименуйте файл .env.sample в .env и отредактируйте параметры:
    ```text
    CACHE_ENABLED=True - использование/неиспользование кеша
    CACHE_LOCATION=redis://host:port - локация redis
    
    SECRET_KEY=key - секретный ключ Django
    
    ENGINE=django.db.backends.postgresql
    NAME=db_name - название базы данных 
    USER=user - имя пользователя базы данных
    PASSWORD=password - пароль пользователя базы данных 
    HOST=host - можно указать localhost
    PORT=port - порт для подключения к базе данных
    
    EMAIL_HOST=email_host - хост почтового сервера(здесь используется yandex)
    EMAIL_PORT=email_port - порт почтового сервера
    EMAIL_HOST_USER=your_email@yandex.ru - ваш email
    EMAIL_HOST_PASSWORD=password - ваш пароль smtp
    EMAIL_USE_TLS=False
    EMAIL_USE_SSL=True
    
    SERVER_EMAIL=EMAIL_HOST_USER
    DEFAULT_FROM_EMAIL=EMAIL_HOST_USER
    ```

### Настройка БД и кэширования:

- Создайте миграции:
  ```text
  python manage.py makemigrations
  ```

- Примените миграции:
  ```text
  python manage.py migrate
  ```

- Если вы хотите использовать данные из фикстур этого проекта, введите команду:
  ```text
  python manage.py loaddata fixtures/*.json
  ```

- Установите Redis:

    - Linux команда:
   ```text
   sudo apt install redis; 
  или 
  sudo yum install redis;
   ```

    - macOS команда:
   ```text
   brew install redis;
   ```

  Windows инструкция:
    - [Перейти на Redis docs](https://redis.io/docs/install/install-redis/install-redis-on-windows/)

## Использование

- Для запуска проекта наберите в терминале команду:
  ```text
  python manage.py runserver
  ```
  перейдите по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)


- Вместе с запуском проекта, автоматически запускается периодический сервис рассылок. Дополнительно делать ничего не
  нужно.


- Для ручного запуска рассылок можно использовать команду:
  ```text
  python manage.py do_mail
  ```
  Она отправит все запущенные рассылки, даже если время их следующей отправки еще не настало.

## Контакты

Ссылка на репозиторий: [https://github.com/EgorShmelev710](https://github.com/EgorShmelev710)




