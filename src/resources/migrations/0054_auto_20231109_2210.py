# Generated by Django 3.2.23 on 2023-11-09 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0053_auto_20231109_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationlevel',
            name='educationLevel_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='educationLevel_el',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='educationLevel_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='educationLevel_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='educationLevel_et',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='educationLevel_fr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='educationLevel_hu',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='educationLevel_it',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='educationLevel_lt',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='educationLevel_nl',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='educationLevel_pt',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='educationlevel',
            name='educationLevel_sv',
            field=models.TextField(null=True),
        ),
    ]
