# Generated by Django 2.1.1 on 2018-09-25 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_custom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_register',
            name='app_path',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
