# Generated by Django 5.0.3 on 2024-03-26 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.CharField(default=1, max_length=65),
            preserve_default=False,
        ),
    ]
