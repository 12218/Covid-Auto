# Generated by Django 4.0.1 on 2022-02-18 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_coordination',
            field=models.CharField(default='', max_length=50),
        ),
    ]
