# Generated by Django 4.1.1 on 2022-09-28 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crazy_book_clubs', '0002_remove_book_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='name',
            field=models.CharField(default='Default', max_length=200),
        ),
    ]
