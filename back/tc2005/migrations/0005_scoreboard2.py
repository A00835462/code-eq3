# Generated by Django 3.2.18 on 2023-03-29 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tc2005', '0004_remove_scoreboard_points'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scoreboard2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='tc2005.user')),
            ],
        ),
    ]
