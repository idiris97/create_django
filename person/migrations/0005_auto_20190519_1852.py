# Generated by Django 2.1.5 on 2019-05-19 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_auto_20190210_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
