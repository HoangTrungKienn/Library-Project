# Generated by Django 4.1.2 on 2022-10-08 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='bookfile',
            field=models.FileField(default=None, upload_to='files'),
        ),
    ]
