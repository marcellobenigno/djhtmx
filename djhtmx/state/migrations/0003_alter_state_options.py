# Generated by Django 4.0.1 on 2022-01-14 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0002_rename_states_state'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='state',
            options={'ordering': ['region', 'name'], 'verbose_name': 'Estado', 'verbose_name_plural': 'Estados'},
        ),
    ]
