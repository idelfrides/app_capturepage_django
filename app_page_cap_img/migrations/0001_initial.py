# Generated by Django 2.2.2 on 2019-06-05 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageCapImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('copy_descricao', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('imgPosition', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=5)),
            ],
            options={
                'verbose_name_plural': 'PageCapImage',
            },
        ),
    ]
