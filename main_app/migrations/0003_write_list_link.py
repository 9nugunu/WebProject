# Generated by Django 3.1.2 on 2020-12-31 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20201230_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='write_list',
            name='link',
            field=models.URLField(default=0, verbose_name='Site URL'),
            preserve_default=False,
        ),
    ]
