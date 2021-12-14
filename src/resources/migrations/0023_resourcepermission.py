# Generated by Django 2.2.10 on 2020-03-18 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resources', '0022_auto_20200317_0832'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourcePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.Resource')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]