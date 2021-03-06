# Generated by Django 3.0.1 on 2019-12-31 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_personsocialmedia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personsocialmedia',
            name='person',
        ),
        migrations.AlterField(
            model_name='personsocialmedia',
            name='social_media',
            field=models.CharField(choices=[('github', 'GitHub'), ('facebook-f', 'Facebook'), ('twitter', 'Twitter'), ('reddit-alien', 'Reddit'), ('linkedin-in', 'LinkedIn'), ('instagram', 'Instagram'), ('youtube', 'YouTube')], max_length=20),
        ),
        migrations.AlterField(
            model_name='personsocialmedia',
            name='url',
            field=models.CharField(max_length=500),
        ),
    ]
