# Generated by Django 5.2 on 2025-04-07 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('def_code', models.CharField(db_index=True, max_length=3)),
                ('start_range', models.BigIntegerField(db_index=True)),
                ('end_range', models.BigIntegerField()),
                ('capacity', models.IntegerField()),
                ('operator', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('territory', models.CharField(max_length=255)),
                ('inn', models.CharField(max_length=20)),
            ],
            options={
                'indexes': [models.Index(fields=['def_code', 'start_range', 'end_range'], name='pic_phonera_def_cod_5c93eb_idx')],
            },
        ),
    ]
