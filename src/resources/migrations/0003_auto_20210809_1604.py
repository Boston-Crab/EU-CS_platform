# Generated by Django 2.2.13 on 2021-08-09 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_approved'),
        ('resources', '0002_resource_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='project',
            field=models.ManyToManyField(to='projects.Project'),
        ),
        migrations.AddField(
            model_name='resource',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='resource',
            name='url',
            field=models.URLField(),
        ),
    ]