# Generated by Django 2.2.4 on 2019-11-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('picture', models.ImageField(upload_to='images/')),
                ('resume', models.FileField(upload_to='resume/')),
                ('about', models.CharField(max_length=5000)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('picture', models.ImageField(upload_to='images/')),
                ('date', models.DateField()),
                ('detail', models.CharField(max_length=3000)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
