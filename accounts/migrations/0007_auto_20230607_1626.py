# Generated by Django 3.2.19 on 2023-06-07 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20230525_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
