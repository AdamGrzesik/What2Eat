# Generated by Django 4.1.2 on 2022-12-11 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='products',
            field=models.ManyToManyField(related_name='products', to='App.product'),
        ),
    ]
