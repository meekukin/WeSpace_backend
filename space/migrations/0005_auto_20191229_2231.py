# Generated by Django 3.0.1 on 2019-12-29 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0004_spaces_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spaces',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
