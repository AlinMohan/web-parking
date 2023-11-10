# Generated by Django 4.1.7 on 2023-11-09 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserId', models.TextField()),
                ('Name', models.CharField(max_length=100)),
                ('Phone', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('VehicleNumber', models.TextField()),
                ('Username', models.TextField()),
                ('Password', models.TextField()),
            ],
        ),
    ]