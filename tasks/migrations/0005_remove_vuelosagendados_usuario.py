# Generated by Django 5.1.1 on 2024-12-02 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_vuelosagendados'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vuelosagendados',
            name='usuario',
        ),
    ]
