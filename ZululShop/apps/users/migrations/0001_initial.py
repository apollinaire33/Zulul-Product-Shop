# Generated by Django 3.1.1 on 2020-09-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=100)),
                ('avatar', models.URLField(blank=True)),
            ],
        ),
    ]
