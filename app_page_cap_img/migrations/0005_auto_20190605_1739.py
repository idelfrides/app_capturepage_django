# Generated by Django 2.2.2 on 2019-06-05 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_page_cap_img', '0004_auto_20190605_1736'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagecapimage',
            old_name='imgPosition',
            new_name='imgage_position',
        ),
    ]