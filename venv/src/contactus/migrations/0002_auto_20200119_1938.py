# Generated by Django 2.1.7 on 2020-01-20 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='Name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='Number',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='Query',
            field=models.TextField(max_length=500),
        ),
    ]
