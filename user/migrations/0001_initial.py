from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kor', models.CharField(max_length=45)),
                ('name_eng', models.CharField(max_length=45, null=True)),
            ],
            options={
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=45)),
                ('password', models.CharField(max_length=200)),
                ('sex', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.country')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
