# Generated by Django 3.2.23 on 2023-11-05 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thememanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topbar',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='thememanager.topbar'),
        ),
    ]
