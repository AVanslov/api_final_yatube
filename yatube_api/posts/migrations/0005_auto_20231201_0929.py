# Generated by Django 3.2.16 on 2023-12-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_rename_follower_follow_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('group', 'pub_date', 'author__username')},
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_subscriber_author_pair'),
        ),
    ]
