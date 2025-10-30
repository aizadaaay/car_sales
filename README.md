# Car Sales

Сайт для продажи автомобилей. Пользователи могут просматривать каталог автомобилей, добавлять новые машины, видеть популярные модели и использовать кредитный калькулятор. 🌐 Доступен онлайн: [https://car-sales-qps2.onrender.com/](https://car-sales-qps2.onrender.com/)

Основные функции включают просмотр каталога автомобилей с фотографиями, фильтрацию и сортировку по марке, цене, году и другим параметрам, добавление новых автомобилей с фото и описанием, прогноз цены автомобиля на основе модели машинного обучения, кредитный калькулятор для расчета ежемесячного платежа, информационные страницы "О нас" и "Контакты". Медиа файлы (изображения авто) хранятся на Cloudinary.

Используемые технологии: Django 4.2+, Python 3.12, PostgreSQL, Cloudinary для хранения медиа файлов, HTML, CSS, JavaScript, Gunicorn для продакшн-сервера.

## Установка локально

1. Клонируем репозиторий и переходим в папку проекта:
```bash
git clone https://github.com/aizadaaay/car_sales.git
cd car_sales
Создаем и активируем виртуальное окружение:

bash
Копировать код
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
Устанавливаем зависимости:

bash
Копировать код
pip install -r requirements.txt
Настраиваем базу данных PostgreSQL в settings.py или через .env:

python
Копировать код
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://USERNAME:PASSWORD@HOST:PORT/DBNAME',
        conn_max_age=600,
        ssl_require=True
    )
}
Настраиваем Cloudinary для хранения медиа файлов:

python
Копировать код
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'ваш_cloud_name',
    'API_KEY': 'ваш_api_key',
    'API_SECRET': 'ваш_api_secret',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_URL = '/media/'  # для совместимости
Применяем миграции:

bash
Копировать код
python manage.py migrate
Создаем суперпользователя:

bash
Копировать код
python manage.py createsuperuser
Запускаем сервер разработки:

bash
Копировать код
python manage.py runserver
Сайт будет доступен по адресу: http://127.0.0.1:8000/
