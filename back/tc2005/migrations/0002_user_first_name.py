# Generated by Django 3.2.18 on 2023-03-29 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tc2005', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=25, null=True),
        ),
    ]