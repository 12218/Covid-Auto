# Generated by Django 4.0.1 on 2022-01-26 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_or_off', models.BooleanField(default=False)),
                ('task_title', models.CharField(max_length=50)),
                ('task_province', models.CharField(max_length=20)),
                ('task_city', models.CharField(max_length=30)),
                ('task_owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_username', models.CharField(default='', max_length=20)),
                ('task_stu_id', models.CharField(default='', max_length=20)),
                ('task_phone', models.CharField(default='', max_length=20)),
                ('task_institution', models.CharField(default='', max_length=20)),
                ('task_form_id', models.CharField(default='', max_length=10)),
                ('vjuid', models.CharField(default='', max_length=20)),
                ('vjvd', models.CharField(default='', max_length=50)),
                ('vt', models.CharField(default='', max_length=20)),
                ('UUkey', models.CharField(default='', max_length=50)),
                ('task_owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
