# Generated by Django 3.1.2 on 2020-11-13 09:47

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QnA_app', '0017_auto_20201113_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qnamodel',
            name='content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
