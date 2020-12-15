from django.db import models


class Survey(models.Model):
    content = models.TextField()
    users   = models.ManyToManyField('user.User', through = 'UserSurvey')

    class Meta:
        db_table = 'surveys'

class UserSurvey(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.DO_NOTHING)
    user   = models.ForeignKey('user.User', on_delete=models.DO_NOTHING)
    time   = models.IntegerField(null=True)
    answer = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'users_surveys'

class InvestType(models.Model):
    content = models.TextField()

    class Meta:
        db_table = 'invest_types'
