# Generated by Django 3.2.23 on 2024-04-12 05:28

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0097_alter_status_status_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('country_name', models.CharField(editable=False, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='projectCountry',
            field=models.ManyToManyField(blank=True, related_name='projects', to='projects.ProjectCountry'),
        ),
    ]
