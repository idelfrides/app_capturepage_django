# Generated by Django 2.2.2 on 2019-06-13 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_page_cap_img', '0020_auto_20190613_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecapimage',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]