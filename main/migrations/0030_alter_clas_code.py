# Generated by Django 4.1.2 on 2023-01-08 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_alter_clas_code_alter_clas_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clas',
            name='code',
            field=models.CharField(default='QNHDW', max_length=5),
        ),
    ]