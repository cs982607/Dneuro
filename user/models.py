from django.db import models

class Country(models.Model):
    name_kor = models.CharField(max_length=45)
    name_eng = models.CharField(max_length=45, null=True)

    class Meta:
        db_table='countries'

class User(models.Model):
    email    = models.EmailField(max_length=45)
    password = models.CharField(max_length=200)
    sex      = models.CharField(max_length=20)
    birthday = models.DateField()
    country  = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    class Meta:
        db_table='users'
