# Generated by Django 3.2.16 on 2023-11-30 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20231129_1558'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='user',
            new_name='follower',
        ),
    ]
