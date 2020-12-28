from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'survey_categories'


class Survey(models.Model):
    content  = models.TextField()
    users    = models.ManyToManyField('user.User', through='UserSurvey')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    
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


class InvestType(models.Model):
    content = models.TextField()

    class Meta:
        db_table = 'invest_types'


class EvasionGrade(models.Model):
    grade    = models.IntegerField(default=1)
    tendency = models.CharField(max_length=45) #경향

    class Meta:
        db_table = 'evasion_grade'
