# Generated by Django 3.1.2 on 2020-10-03 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QnA_app', '0002_auto_20201003_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qnamodel',
            name='author',
            field=models.CharField(max_length=10),
        ),
    ]
