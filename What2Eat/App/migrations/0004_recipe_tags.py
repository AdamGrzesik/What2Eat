# Generated by Django 4.1.2 on 2022-12-11 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_recipe_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.JSONField(default='nic'),
        ),
    ]
