# Generated by Django 3.2.23 on 2023-11-08 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0087_auto_20231108_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_de',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_el',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_es',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_et',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_fr',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_hu',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_it',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_lt',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_nl',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_pt',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description_sv',
            field=models.TextField(null=True),
        ),
    ]