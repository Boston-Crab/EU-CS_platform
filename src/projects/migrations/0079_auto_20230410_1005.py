# Generated by Django 2.2.10 on 2023-04-10 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0078_merge_20230408_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchstats',
            name='search',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]