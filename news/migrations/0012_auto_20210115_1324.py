# Generated by Django 3.1.5 on 2021-01-15 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20210115_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]