# Generated by Django 4.2.5 on 2023-10-07 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_forum_created_at_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='mail',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
