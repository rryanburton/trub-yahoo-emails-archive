# Generated by Django 3.0.2 on 2020-01-02 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trubYahooArchive', '0002_auto_20200102_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trubemail',
            name='userId',
        ),
        migrations.AlterField(
            model_name='trubemail',
            name='sender',
            field=models.CharField(blank=True, default='', max_length=250),
            preserve_default=False,
        ),
    ]