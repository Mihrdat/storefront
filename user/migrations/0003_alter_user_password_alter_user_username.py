# Generated by Django 4.1.2 on 2023-01-23 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='!dW3i1MCWDt2OmA1wUk3Ntz5g29u4MYOdPFscrONQ', max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]