# Generated by Django 3.2.9 on 2021-11-25 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211125_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_valid',
            field=models.CharField(blank=True, choices=[(False, 'رد'), (True, 'تائید')], max_length=10, verbose_name='اعتبارسنجی'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='is_valid',
            field=models.CharField(blank=True, choices=[(False, 'رد'), (True, 'تائید')], max_length=10, verbose_name='اعتبارسنجی'),
        ),
    ]