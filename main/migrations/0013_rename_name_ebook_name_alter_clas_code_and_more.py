# Generated by Django 4.1.2 on 2022-11-05 12:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_alter_clas_code_ebook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ebook',
            old_name='Name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='clas',
            name='code',
            field=models.CharField(default='XnpMr', max_length=5),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='book',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='students',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
