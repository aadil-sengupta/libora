# Generated by Django 4.1.2 on 2022-11-13 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0019_reading_day_user_alter_clas_code_readbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='clas',
            name='goal',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clas',
            name='code',
            field=models.CharField(default='RGiYQ', max_length=5),
        ),
        migrations.AlterField(
            model_name='readbook',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='readbook',
            name='time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='readbook',
            name='words',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reading_day',
            name='time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='reading_day',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reading_day',
            name='words',
            field=models.IntegerField(default=0),
        ),
    ]
