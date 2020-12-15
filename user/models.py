from django.db import models

class Country(models.Model):
    name_kor = models.CharField(max_length=45)
<<<<<<< HEAD
    name_eng = models.CharField(max_length=45)
=======
    name_eng = models.CharField(max_length=45, null=True)
>>>>>>> 77d7ac5 (ADD: user.view 작성 및 unit test 완료)

    class Meta:
        db_table='countries'

class User(models.Model):
    email    = models.EmailField(max_length=45)
    password = models.CharField(max_length=200)
    sex      = models.CharField(max_length=20)
<<<<<<< HEAD
    birthday = models.DateField
=======
    birthday = models.DateField()
>>>>>>> 77d7ac5 (ADD: user.view 작성 및 unit test 완료)
    country  = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    class Meta:
        db_table='users'

