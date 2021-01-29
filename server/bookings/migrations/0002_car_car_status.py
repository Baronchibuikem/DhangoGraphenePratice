# Generated by Django 3.1.5 on 2021-01-26 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_status',
            field=models.CharField(choices=[('NOT_LOADING', 'NOT_LOADING'), ('LOADING', 'LOADING'), ('ENROUTE', 'ENROUTE'), ('BROKEN_DOWN', 'BROKEN_DOWN'), ('COMPLETED', 'COMPLETED')], default='NOT_LOADING', max_length=100),
        ),
    ]
