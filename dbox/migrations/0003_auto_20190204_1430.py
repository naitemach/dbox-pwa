# Generated by Django 2.0.10 on 2019-02-04 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbox', '0002_auto_20190203_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='doc_id',
            new_name='doc',
        ),
    ]
