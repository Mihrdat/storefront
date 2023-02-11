# Generated by Django 4.1.2 on 2023-02-11 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0014_alter_order_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderstatuslog',
            name='performer',
        ),
        migrations.AddField(
            model_name='orderstatuslog',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='orderstatuslog',
            name='current_status',
            field=models.IntegerField(choices=[(1, 'Pending'), (2, 'Processing'), (3, 'Awaiting Fulfillment'), (4, 'Fulfilled'), (5, 'Shipped'), (6, 'Delivered'), (7, 'Cancelled'), (8, 'Refunded'), (9, 'On Hold'), (10, 'Returned'), (11, 'Exchange Requested'), (12, 'Completed')]),
        ),
        migrations.AlterField(
            model_name='orderstatuslog',
            name='previous_status',
            field=models.IntegerField(choices=[(1, 'Pending'), (2, 'Processing'), (3, 'Awaiting Fulfillment'), (4, 'Fulfilled'), (5, 'Shipped'), (6, 'Delivered'), (7, 'Cancelled'), (8, 'Refunded'), (9, 'On Hold'), (10, 'Returned'), (11, 'Exchange Requested'), (12, 'Completed')]),
        ),
    ]