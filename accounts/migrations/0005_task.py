# Generated by Django 3.1.3 on 2020-11-20 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_delete_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256, null=True)),
                ('description', models.TextField(null=True)),
                ('status', models.CharField(choices=[('NEW', 'New'), ('OPN', 'Open'), ('COM', 'Complete'), ('SUS', 'Suspension'), ('CNX', 'Canceled')], default=0, max_length=3)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('priority', models.CharField(choices=[('LW', 'Low'), ('MD', 'Medium'), ('HI', 'High'), ('CR', 'Critical')], default=0, max_length=2)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('assigned_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
