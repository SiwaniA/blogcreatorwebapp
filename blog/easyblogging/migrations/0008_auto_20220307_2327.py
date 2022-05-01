# Generated by Django 3.2.9 on 2022-03-07 17:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('easyblogging', '0007_auto_20220307_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='liked',
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='likes',
            field=models.ManyToManyField(related_name='blogpost_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
