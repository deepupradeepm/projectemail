# Generated by Django 2.1.7 on 2019-04-25 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_modle',
            name='image',
            field=models.ImageField(default=False, upload_to='emp/'),
        ),
    ]
