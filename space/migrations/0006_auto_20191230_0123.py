# Generated by Django 3.0.1 on 2019-12-30 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0005_auto_20191230_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories_space',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='categories_space',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
