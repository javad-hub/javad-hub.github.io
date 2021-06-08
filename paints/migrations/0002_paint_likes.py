# Generated by Django 3.2.3 on 2021-05-31 15:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paints', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paint',
            name='likes',
            field=models.ManyToManyField(related_name='paints', to=settings.AUTH_USER_MODEL),
        ),
    ]
