# Тестовое задание: Проверка оператора и региона по номеру телефона

![Django](https://img.shields.io/badge/Django-5.2-brightgreen)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue)
![Docker](https://img.shields.io/badge/Docker-blue)

Веб-приложение для определения оператора связи, региона и других данных по номеру телефона на основе официальных данных с сайта https://opendata.digital.gov.ru/

## Особенности

- Автоматическое обновление данных каждые 12 часов
- Поиск по номеру в формате +7XXXXXXXXXX
- Полная контейнеризация (Docker)
- Валидация ввода

## Технологии

- **Backend**: Django 5.2
- **Database**: PostgreSQL 17
- **Infrastructure**: 
  - Docker + Docker Compose
  - Gunicorn
  - Cron для автоматического обновления

## Требования

- Docker 25.0+
- Docker Compose 2.20+

## Быстрый старт

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/phone-info-checker.git
```
2. Создайте файл окружения .env и заполните его по шаблону .env.template
3. Запустите приложение:
```bash
docker-compose up -d --build
```

## Принудительное обновление данных
```bash
docker-compose exec cron python manage.py update_data
```

## Остановка
```bash
docker-compose down -v
```
