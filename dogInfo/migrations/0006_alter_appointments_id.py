# Generated by Django 3.2.9 on 2021-11-21 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogInfo', '0005_appointments_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
