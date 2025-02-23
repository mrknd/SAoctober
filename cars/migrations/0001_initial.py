# Generated by Django 3.2 on 2024-09-30 19:02

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand_name', models.CharField(max_length=50, verbose_name='Марка автомобіля')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug (Не редагувати)')),
                ('car_brand_image', models.ImageField(upload_to='car_brand_images', verbose_name='Фото марки авто')),
                ('is_featured', models.BooleanField(default=False, verbose_name='Показувати на головній сторінці')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Марка Авто',
                'ordering': ['car_brand_name'],
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('price', models.IntegerField(verbose_name='Ціна')),
                ('car_title_photo', models.ImageField(upload_to='car_photos', verbose_name='Головне фото')),
                ('car_photo_1', models.ImageField(blank=True, null=True, upload_to='car_photos', verbose_name='Фото 2')),
                ('car_photo_2', models.ImageField(blank=True, null=True, upload_to='car_photos', verbose_name='Фото 3')),
                ('car_photo_3', models.ImageField(blank=True, null=True, upload_to='car_photos', verbose_name='Фото 4')),
                ('car_photo_4', models.ImageField(blank=True, null=True, upload_to='car_photos', verbose_name='Фото 5')),
                ('car_photo_5', models.ImageField(blank=True, null=True, upload_to='car_photos', verbose_name='Фото 6')),
                ('car_photo_6', models.ImageField(blank=True, null=True, upload_to='car_photos', verbose_name='Фото 7')),
                ('car_photo_7', models.ImageField(blank=True, null=True, upload_to='car_photos', verbose_name='Фото 8')),
                ('car_photo_8', models.ImageField(blank=True, null=True, upload_to='car_photos', verbose_name='Фото 9')),
                ('mileage', models.IntegerField(verbose_name='Пробіг')),
                ('year', models.IntegerField(verbose_name='Рік випуску')),
                ('engine', models.CharField(blank=True, max_length=100, null=True, verbose_name='Двигун')),
                ('fuel_type', models.CharField(choices=[('Дизель', 'Дизель'), ('Бензин', 'Бензин'), ('Гібрид', 'Гібрид'), ('Електро', 'Електро')], max_length=50, verbose_name='Тип палива')),
                ('transmission', models.CharField(choices=[('Автомат', 'Автомат'), ('Механіка', 'Механіка')], max_length=100, verbose_name='Тип коробки передач')),
                ('body_style', models.CharField(choices=[('Седан', 'Седан'), ('Хетчбек', 'Хетчбек'), ('Універсал', 'Універсал'), ('Купе', 'Купе'), ('Кросовер', 'Кросовер'), ('Кабріолет', 'Кабріолет'), ('Родстер', 'Родстер'), ('Позашляховик', 'Позашляховик'), ('Мінівен', 'Мінівен'), ('Пікап', 'Пікап'), ('Мото', 'Мото')], max_length=100, verbose_name='Тип кузова')),
                ('wheel_drive', models.CharField(choices=[('Повний', 'Повний'), ('Передній', 'Передній'), ('Задній', 'Задній')], max_length=100, verbose_name='Привід')),
                ('color', models.CharField(max_length=100, verbose_name='Колір')),
                ('interior_color', models.CharField(max_length=100, verbose_name='Колір салону')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Опис')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('in_stock', models.BooleanField(default=False, verbose_name='Авто в наявності')),
                ('car_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.carbrand', verbose_name='Марка авто')),
            ],
            options={
                'verbose_name_plural': 'Всі Авто',
                'ordering': ['-updated_at'],
            },
        ),
    ]
