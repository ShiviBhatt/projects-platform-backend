# Generated by Django 2.2.6 on 2020-01-23 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scprojects', '0006_auto_20200123_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='lead',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leads', to=settings.AUTH_USER_MODEL),
        ),
    ]