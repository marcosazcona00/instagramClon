# Generated by Django 3.1.7 on 2021-02-20 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='url_foto',
            field=models.TextField(blank=True),
        ),
    ]
