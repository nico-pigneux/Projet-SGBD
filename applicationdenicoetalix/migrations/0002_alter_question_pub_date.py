# Generated by Django 5.0 on 2023-12-06 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicationdenicoetalix', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date publishe'),
        ),
    ]