# Generated by Django 3.2 on 2021-05-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("form", "0007_auto_20210515_1331"),
    ]

    operations = [
        migrations.AddField(
            model_name="courier",
            name="profit_sell_percentage",
            field=models.CharField(
                blank=True,
                max_length=250,
                null=True,
                verbose_name="Profit Sell Percentage",
            ),
        ),
        migrations.AddField(
            model_name="sellbuycourier",
            name="fuel_surcharge_dhl_percentage",
            field=models.CharField(
                blank=True,
                max_length=250,
                null=True,
                verbose_name="Fuel Surcharge DHL Percentage",
            ),
        ),
        migrations.AddField(
            model_name="sellbuycourier",
            name="fuel_surcharge_ups_percentage",
            field=models.CharField(
                blank=True,
                max_length=250,
                null=True,
                verbose_name="Fuel Surcharge UPS Percentage",
            ),
        ),
    ]
