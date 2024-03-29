# Generated by Django 2.2.2 on 2019-06-11 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_page_cap_img', '0012_auto_20190610_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('arquivo_pdf', models.FileField(upload_to='files/')),
            ],
            options={
                'verbose_name_plural': 'Medias ',
            },
        ),
        migrations.DeleteModel(
            name='Arquivos',
        ),
        migrations.AlterField(
            model_name='pagecapimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
