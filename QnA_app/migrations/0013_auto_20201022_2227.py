# Generated by Django 3.1.2 on 2020-10-22 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QnA_app', '0012_auto_20201018_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='modified_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='qnamodel',
            name='modified_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
