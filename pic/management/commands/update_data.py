import requests
import csv
from django.core.management.base import BaseCommand
from django.db import transaction
from pic.models import PhoneRange

CSV_URLS = [
    'https://opendata.digital.gov.ru/downloads/ABC-3xx.csv',
    'https://opendata.digital.gov.ru/downloads/ABC-4xx.csv',
    'https://opendata.digital.gov.ru/downloads/ABC-8xx.csv',
    'https://opendata.digital.gov.ru/downloads/DEF-9xx.csv'
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/csv',
    'Accept-Language': 'ru-RU,ru;q=0.9',
    'Referer': 'https://opendata.digital.gov.ru/'
}


class Command(BaseCommand):
    help = 'Обновление базы (происходит ежедневно)'

    def handle(self, *args, **options):
        with transaction.atomic():
            PhoneRange.objects.all().delete()

            for url in CSV_URLS:
                try:
                    response = requests.get(url, headers=HEADERS)
                    response.raise_for_status()

                    response.encoding = 'utf-8-sig'
                    reader = csv.DictReader(response.text.splitlines(), delimiter=';')

                    bulk_list = []
                    for row in reader:
                        bulk_list.append(PhoneRange(
                            def_code=row['АВС/ DEF'],
                            start_range=int(row['От']),
                            end_range=int(row['До']),
                            capacity=int(row['Емкость']),
                            operator=row['Оператор'],
                            region=row['Регион'],
                            territory=row['Территория ГАР'],
                            inn=row['ИНН']
                        ))

                    PhoneRange.objects.bulk_create(bulk_list, batch_size=1000)
                    self.stdout.write(f'Обработан файл: {url}')

                except requests.exceptions.RequestException as e:
                    self.stdout.write(self.style.ERROR(
                        f'Ошибка при загрузке {url}: {str(e)}'
                    ))
                    continue

                self.stdout.write(self.style.SUCCESS(f'Успешно обновлено {len(bulk_list)} записей'))