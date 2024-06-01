# Generated by Django 5.0.6 on 2024-06-01 21:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Город')),
                ('street', models.CharField(blank=True, max_length=150, null=True, verbose_name='Улица')),
                ('house_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Номер дома')),
                ('creation_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
                'ordering': ['email'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название продукта')),
                ('product_model', models.CharField(max_length=100, verbose_name='Модель')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Дата выхода')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Цена')),
                ('creation_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200, verbose_name='Название')),
                ('types_sellers', models.IntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], default=0, verbose_name='Тип сети')),
                ('level', models.PositiveIntegerField(verbose_name='Уровень поставки')),
                ('debt', models.FloatField(blank=True, null=True, verbose_name='Задолженность')),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('creation_owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.company', verbose_name='Поставщик')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.contacts', verbose_name='Контакты')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'ordering': ['company_name'],
            },
        ),
    ]