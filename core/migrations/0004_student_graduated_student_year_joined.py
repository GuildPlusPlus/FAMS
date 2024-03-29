# Generated by Django 4.2 on 2023-04-16 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_person_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='graduated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='year_joined',
            field=models.PositiveIntegerField(default=2020),
            preserve_default=False,
        ),
    ]
