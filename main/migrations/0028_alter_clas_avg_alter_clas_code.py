# Generated by Django 4.1.2 on 2022-11-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_clas_avg_alter_clas_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clas',
            name='avg',
            field=models.DecimalField(decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='clas',
            name='code',
            field=models.CharField(default='APjsi', max_length=5),
        ),
    ]
