# Generated by Django 3.0.2 on 2020-01-03 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trubYahooArchive', '0009_trubemail_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trubemail',
            name='postDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
