# Generated by Django 4.2.2 on 2023-06-16 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'myuser_schema"."userdetails_table',
            },
        ),
    ]