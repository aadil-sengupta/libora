# Generated by Django 4.1.2 on 2022-11-16 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_rename_time_ebook_avg_alter_clas_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clas',
            name='code',
            field=models.CharField(default='Ug52E', max_length=5),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='avg',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='words',
            field=models.IntegerField(null=True),
        ),
    ]
