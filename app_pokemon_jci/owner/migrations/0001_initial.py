# Generated by Django 5.1.3 on 2024-11-10 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.IntegerField(default=0)),
                ('pais', models.CharField(max_length=40)),
                ('desactivado', models.BooleanField(default=False)),
            ],
        ),
    ]
