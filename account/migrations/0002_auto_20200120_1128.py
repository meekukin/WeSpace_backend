# Generated by Django 3.0.1 on 2020-01-20 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('space', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservations',
            name='space',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='space.Spaces'),
        ),
        migrations.AddField(
            model_name='reservations',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Accounts'),
        ),
        migrations.AddField(
            model_name='likes',
            name='space',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='space.Spaces'),
        ),
        migrations.AddField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Accounts'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='like',
            field=models.ManyToManyField(through='account.Likes', to='space.Spaces'),
        ),
    ]
