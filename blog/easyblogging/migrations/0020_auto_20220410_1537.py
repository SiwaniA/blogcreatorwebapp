# Generated by Django 3.2.9 on 2022-04-10 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easyblogging', '0019_auto_20220330_0154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogmodel',
            old_name='upload_to',
            new_name='published',
        ),
        migrations.RemoveField(
            model_name='category',
            name='cat_image',
        ),
    ]
