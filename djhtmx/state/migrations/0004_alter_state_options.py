# Generated by Django 4.0.1 on 2022-01-14 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0003_alter_state_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name': 'Estado', 'verbose_name_plural': 'Estados'},
        ),
    ]
