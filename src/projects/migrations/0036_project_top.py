# Generated by Django 2.2.10 on 2020-05-08 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0035_project_doingathome'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='top',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]