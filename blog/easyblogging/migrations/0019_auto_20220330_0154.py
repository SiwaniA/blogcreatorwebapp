# Generated by Django 3.2.9 on 2022-03-29 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easyblogging', '0018_alter_blogmodel_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
