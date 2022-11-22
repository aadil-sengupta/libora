# Generated by Django 4.1.2 on 2022-11-07 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_ebook_cover_alter_clas_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clas',
            name='code',
            field=models.CharField(default='3K6Jp', max_length=5),
        ),
        migrations.RemoveField(
            model_name='ebook',
            name='clas',
        ),
        migrations.AddField(
            model_name='ebook',
            name='clas',
            field=models.ManyToManyField(to='main.clas'),
        ),
    ]
