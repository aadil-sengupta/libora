# Generated by Django 4.1.2 on 2022-11-02 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clas',
            name='code',
            field=models.UUIDField(default='WhBLT', editable=False),
        ),
    ]
