# Generated by Django 4.2.10 on 2024-04-22 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_product_genre_three_alter_product_genre_two'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='genre_three',
        ),
        migrations.RemoveField(
            model_name='product',
            name='genre_two',
        ),
    ]
