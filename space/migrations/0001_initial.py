
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('amenity', models.CharField(max_length=300)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'amenities',
            },
        ),
        migrations.CreateModel(
            name='Space_Amenities',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('amenity', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='space.Amenities')),
            ],
            options={
                'db_table': 'space_amenities',
            },
        ),
        migrations.CreateModel(
            name='Space_Categories',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'space_categories',
            },
        ),
        migrations.CreateModel(
            name='Spaces',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_intro', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('long_intro', models.TextField()),
                ('location', models.CharField(max_length=300)),
                ('min_time', models.CharField(max_length=10, null=True)),
                ('min_guest', models.CharField(max_length=10, null=True)),
                ('open_time', models.CharField(max_length=10)),
                ('close_time', models.CharField(max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('amenity_space', models.ManyToManyField(
                    through='space.Space_Amenities', to='space.Amenities')),
                ('host', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Hosts')),
            ],
            options={
                'db_table': 'spaces',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('space', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='space.Spaces')),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.AddField(
            model_name='space_amenities',
            name='space',
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to='space.Spaces'),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('image', models.URLField(max_length=2500)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('space', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='space.Spaces')),
                ('user', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Accounts')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='Qeustion',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('space', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='space.Spaces')),
                ('user', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Accounts')),
            ],
        ),
        migrations.CreateModel(
            name='Notices',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.CharField(max_length=300)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('space', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='space.Spaces')),
            ],
            options={
                'db_table': 'notice',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('space_image', models.URLField(max_length=2500)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('space', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='space.Spaces')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday', models.DateTimeField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('space', models.ForeignKey(
                    null=True, on_delete=django.db.models.deletion.SET_NULL, to='space.Spaces')),
            ],
            options={
                'db_table': 'holiday',
            },
        ),
    ]
