# Generated by Django 3.2.9 on 2022-03-07 19:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('easyblogging', '0008_auto_20220307_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
