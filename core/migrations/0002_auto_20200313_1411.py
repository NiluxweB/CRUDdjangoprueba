# Generated by Django 3.0.1 on 2020-03-13 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='genero',
            field=models.CharField(max_length=100),
        ),
    ]
