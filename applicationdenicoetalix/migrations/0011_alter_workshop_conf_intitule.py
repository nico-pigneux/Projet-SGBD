# Generated by Django 5.0 on 2024-01-06 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicationdenicoetalix', '0010_rename_délai_de_notification_après_soummission_categoriedesoumission_delai_de_notification_apres_sou'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='conf_intitule',
            field=models.ForeignKey(db_column='Conf_intitule', on_delete=django.db.models.deletion.DO_NOTHING, to='applicationdenicoetalix.conference'),
        ),
    ]
