# Generated by Django 5.0 on 2023-12-06 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicationdenicoetalix', '0002_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
