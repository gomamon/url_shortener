# Generated by Django 2.2.9 on 2020-01-08 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='recent_url',
            field=models.CharField(default='zzzzzzzz', max_length=8),
        ),
    ]
