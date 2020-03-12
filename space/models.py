from django.db import models
from account.models import Hosts, Accounts


class Space(models.Model):
    title = models.CharField(max_length=100)
    short_intro = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    long_intro = models.TextField()
    location = models.CharField(max_length=300)
    host = models.ForeignKey(
        'account.Hosts', on_delete=models.SET_NULL, null=True)
    min_time = models.CharField(max_length=10, null=True)
    min_guest = models.CharField(max_length=10, null=True)
    open_time = models.CharField(max_length=10)
    close_time = models.CharField(max_length=10)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    amenity_space = models.ManyToManyField(
        'Amenities', through='Space_Amenities')

    class Meta:
        db_table = 'spaces'


class Amenity(models.Model):
    amenity = models.CharField(max_length=300)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'amenities'


class Holiday(models.Model):
    holiday = models.DateTimeField()
    space = models.ForeignKey('Spaces', on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'holiday'


class SpaceCategory(models.Model):
    category = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'space_categories'


class Notice(models.Model):
    notice = models.CharField(max_length=300)
    space = models.ForeignKey('Spaces', on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notices'


class SpaceAmenity(models.Model):
    amenity = models.ForeignKey(
        'Amenities', on_delete=models.SET_NULL, null=True)
    space = models.ForeignKey(
        'Spaces', on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'space_amenities'


class Question(models.Model):
    space = models.ForeignKey(
        'Spaces', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(
        'account.Accounts', on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Mata:
        db_table = 'questions'


class Review(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.SET_NULL, null=True)
    space = models.ForeignKey(Spaces, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    image = models.URLField(max_length=2500)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reviews'


class Tag(models.Model):
    tag = models.CharField(max_length=30)
    space = models.ForeignKey(Spaces, on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tags'


class Image(models.Model):
    space_image = models.URLField(max_length=2500)
    space = models.ForeignKey(Spaces, on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'images'
