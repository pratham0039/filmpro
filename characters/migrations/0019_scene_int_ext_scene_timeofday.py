# Generated by Django 4.2.6 on 2023-10-26 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0018_scenedurationremark_shotno'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene',
            name='int_ext',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scene',
            name='timeofday',
            field=models.TextField(blank=True, null=True),
        ),
    ]
