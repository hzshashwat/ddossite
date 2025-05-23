# Generated by Django 5.2 on 2025-05-18 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blockedip',
            options={'ordering': ['-created_at'], 'verbose_name': 'Blocked IP', 'verbose_name_plural': 'Blocked IPs'},
        ),
        migrations.RenameField(
            model_name='blockedip',
            old_name='detected_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='blockedip',
            old_name='ip_address',
            new_name='ip',
        ),
    ]
