# Generated by Django 4.1.2 on 2022-11-06 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_rename_name_ebook_name_alter_clas_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebook',
            name='cover',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='clas',
            name='code',
            field=models.CharField(default='MGsqd', max_length=5),
        ),
    ]
