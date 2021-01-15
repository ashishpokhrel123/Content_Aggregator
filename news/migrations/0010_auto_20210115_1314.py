# Generated by Django 3.1.5 on 2021-01-15 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20210115_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='subscrition',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.category'),
        ),
    ]