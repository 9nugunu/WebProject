# Generated by Django 3.1.2 on 2020-10-04 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QnA_app', '0005_auto_20201004_0210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='create_date',
        ),
        migrations.AddField(
            model_name='answer',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
