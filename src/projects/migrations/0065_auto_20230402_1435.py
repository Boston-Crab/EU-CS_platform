# Generated by Django 2.2.28 on 2023-04-02 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0064_stats_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='totalLikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stats',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(auto_now_add=True, null=True)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]