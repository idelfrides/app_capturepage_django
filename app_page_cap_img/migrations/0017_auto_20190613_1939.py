# Generated by Django 2.2.2 on 2019-06-13 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_page_cap_img', '0016_auto_20190610_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracao',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='configuracao',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
