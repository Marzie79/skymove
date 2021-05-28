# Generated by Django 3.2 on 2021-05-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("form", "0009_auto_20210528_1301"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="courier",
            name="buy_cost",
        ),
        migrations.RemoveField(
            model_name="courier",
            name="sell_cost_prof",
        ),
        migrations.AddField(
            model_name="courier",
            name="buy_cust",
            field=models.IntegerField(blank=True, null=True, verbose_name="Buy_Cust"),
        ),
        migrations.AddField(
            model_name="courier",
            name="sell_cust_prof",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Sell_Cust_Prof"
            ),
        ),
    ]