# Generated by Django 2.2.2 on 2019-06-05 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_page_cap_img', '0007_auto_20190605_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecapimage',
            name='copy_descricao',
            field=models.TextField(default='Sua Copy descrição aqui.'),
        ),
        migrations.AlterField(
            model_name='pagecapimage',
            name='headline',
            field=models.TextField(default='Coloque sua Headline aqui.'),
        ),
    ]
