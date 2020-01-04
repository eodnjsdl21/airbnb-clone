# Generated by Django 2.2.5 on 2020-01-01 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20200102_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('canceled', 'canceled'), ('pending', 'pending'), ('confirmed', 'confirmed')], default='pending', max_length=12),
        ),
    ]
