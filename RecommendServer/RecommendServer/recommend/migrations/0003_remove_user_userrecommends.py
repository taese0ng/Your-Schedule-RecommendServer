# Generated by Django 3.0.6 on 2020-06-11 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0002_user_userrecommends'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userRecommends',
        ),
    ]
