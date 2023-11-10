# Generated by Django 3.2.23 on 2023-11-08 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0084_auto_20231108_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='difficultylevel',
            name='difficultyLevel_de',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='difficultylevel',
            name='difficultyLevel_el',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='difficultylevel',
            name='difficultyLevel_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='difficultylevel',
            name='difficultyLevel_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='difficultylevel',
            name='difficultyLevel_et',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='difficultylevel',
            name='difficultyLevel_fr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='difficultylevel',
            name='difficultyLevel_hu',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='difficultylevel',
            name='difficultyLevel_it',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='difficultylevel',
            name='difficultyLevel_lt',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='difficultylevel',
            name='difficultyLevel_nl',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='difficultylevel',
            name='difficultyLevel_pt',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='difficultylevel',
            name='difficultyLevel_sv',
            field=models.TextField(null=True),
        ),
    ]
