# Generated by Django 4.2.1 on 2023-06-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veges', '0002_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_view_count',
            field=models.IntegerField(default=1),
        ),
    ]
