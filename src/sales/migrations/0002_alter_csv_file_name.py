# Generated by Django 3.2 on 2021-04-17 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv',
            name='file_name',
            field=models.FileField(upload_to='csv'),
        ),
    ]