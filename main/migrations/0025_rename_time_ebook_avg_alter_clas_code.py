# Generated by Django 4.1.2 on 2022-11-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_ebook_description_alter_clas_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ebook',
            old_name='time',
            new_name='avg',
        ),
        migrations.AlterField(
            model_name='clas',
            name='code',
            field=models.CharField(default='EcWWk', max_length=5),
        ),
    ]
