# Generated by Django 2.2.13 on 2021-09-20 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_translateddescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='translatedDescriptions',
            field=models.ManyToManyField(to='projects.TranslatedDescription'),
        ),
    ]