# Generated by Django 4.1.7 on 2023-03-03 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requests_history',
            name='data',
            field=models.TextField(),
        ),
    ]
