# Generated by Django 2.2.2 on 2019-06-13 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_page_cap_img', '0021_auto_20190613_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracao',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
