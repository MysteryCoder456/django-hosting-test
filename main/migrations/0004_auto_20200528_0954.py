# Generated by Django 3.0.6 on 2020-05-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200528_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
