# Generated by Django 2.1.7 on 2019-04-25 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Modle',
            fields=[
                ('idno', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('cno', models.IntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]