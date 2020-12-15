from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'surveys',
            },
        ),
        migrations.CreateModel(
            name='UserSurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(null=True)),
                ('answer', models.CharField(max_length=45, null=True)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='survey.survey')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.user')),
            ],
            options={
                'db_table': 'users_surveys',
            },
        ),
        migrations.AddField(
            model_name='survey',
            name='users',
            field=models.ManyToManyField(through='survey.UserSurvey', to='user.User'),
        ),
    ]
