# Generated by Django 4.2.11 on 2024-07-08 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_item_height_alter_item_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='height',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='weight',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
