# Generated by Django 3.2.4 on 2021-07-04 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210704_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.CharField(max_length=10),
        ),
    ]