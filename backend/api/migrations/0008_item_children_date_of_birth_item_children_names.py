# Generated by Django 4.2.11 on 2024-07-05 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_item_address_item_barangay_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='children_date_of_birth',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='children_names',
            field=models.TextField(blank=True, null=True),
        ),
    ]