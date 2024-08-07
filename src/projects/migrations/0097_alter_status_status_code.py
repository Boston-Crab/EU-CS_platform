# Generated by Django 3.2.23 on 2024-03-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0096_alter_status_status_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status_code',
            field=models.CharField(choices=[('not_started', 'Not yet started'), ('periodically_active', 'Periodically Active'), ('active', 'Active'), ('on_hold', 'On Hold'), ('completed', 'Completed'), ('abandoned', 'Abandoned')], default='active', max_length=100),
        ),
    ]
