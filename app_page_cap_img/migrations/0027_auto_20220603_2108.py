# Generated by Django 2.2.7 on 2022-06-03 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_page_cap_img', '0026_pagecapimage_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadsemail',
            name='email',
            field=models.EmailField(default='idelfridesjorgepapai@gmail.com', max_length=254),
        ),
    ]
