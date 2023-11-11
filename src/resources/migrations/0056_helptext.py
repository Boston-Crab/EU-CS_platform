# Generated by Django 3.2.23 on 2023-11-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0055_auto_20231109_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_es', models.CharField(max_length=200, null=True)),
                ('title_fr', models.CharField(max_length=200, null=True)),
                ('title_de', models.CharField(max_length=200, null=True)),
                ('title_el', models.CharField(max_length=200, null=True)),
                ('title_hu', models.CharField(max_length=200, null=True)),
                ('title_it', models.CharField(max_length=200, null=True)),
                ('title_lt', models.CharField(max_length=200, null=True)),
                ('title_pt', models.CharField(max_length=200, null=True)),
                ('title_sv', models.CharField(max_length=200, null=True)),
                ('title_et', models.CharField(max_length=200, null=True)),
                ('title_nl', models.CharField(max_length=200, null=True)),
                ('slug', models.CharField(max_length=200)),
                ('paragraph', models.TextField()),
                ('paragraph_en', models.TextField(null=True)),
                ('paragraph_es', models.TextField(null=True)),
                ('paragraph_fr', models.TextField(null=True)),
                ('paragraph_de', models.TextField(null=True)),
                ('paragraph_el', models.TextField(null=True)),
                ('paragraph_hu', models.TextField(null=True)),
                ('paragraph_it', models.TextField(null=True)),
                ('paragraph_lt', models.TextField(null=True)),
                ('paragraph_pt', models.TextField(null=True)),
                ('paragraph_sv', models.TextField(null=True)),
                ('paragraph_et', models.TextField(null=True)),
                ('paragraph_nl', models.TextField(null=True)),
            ],
        ),
    ]
