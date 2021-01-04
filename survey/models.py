from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'survey_categories'


class EffectiveDate(models.Model):
    start_at = models.DateField(null=True)
    end_at   = models.DateField(null=True)

    class Meta:
        db_table = 'effective_dates'


class Survey(models.Model):
    content         = models.TextField()
    users           = models.ManyToManyField('user.User', through='UserSurvey')
    category        = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    effective_date  = models.ForeignKey(EffectiveDate, on_delete=models.DO_NOTHING, default=1)
    
    class Meta:
        db_table = 'surveys'


class UserSurvey(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.DO_NOTHING)
    user   = models.ForeignKey('user.User', on_delete=models.DO_NOTHING)
    time   = models.IntegerField(null=True)
    answer = models.CharField(max_length=45, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users_surveys'


class Result(models.Model):
    user            = models.ForeignKey('user.User', on_delete=models.DO_NOTHING)
    data            = models.TextField(null=True)
    effective_date  = models.ForeignKey(EffectiveDate, on_delete=models.DO_NOTHING, default=1)

    class Meta:
        db_table = 'results'


class Invest_Type(models.Model):
    content = models.TextField()

    class Meta:
        db_table = 'invest_types'


class EvasionGrade(models.Model):
    grade    = models.IntegerField(default=1)
    tendency = models.CharField(max_length=45) #경향

    class Meta:
        db_table = 'evasion_grade'
