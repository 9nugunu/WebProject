# Generated by Django 3.1.2 on 2020-10-03 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QnA_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qnamodel',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='qnamodel',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qnamodel',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qnamodel',
            name='docfile',
            field=models.FileField(default=1, upload_to='documents/%Y/%m/%d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qnamodel',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]