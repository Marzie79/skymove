# Generated by Django 3.2 on 2021-05-14 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("form", "0002_alter_shipment_active"),
    ]

    operations = [
        migrations.RenameField(
            model_name="baseform",
            old_name="Consignee",
            new_name="consignee",
        ),
        migrations.RemoveField(
            model_name="mandatory",
            name="activity_type",
        ),
        migrations.RemoveField(
            model_name="shipment",
            name="mandatory",
        ),
        migrations.RemoveField(
            model_name="shipment",
            name="optional",
        ),
        migrations.AddField(
            model_name="shipment",
            name="buy_mandatory",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="mandatory_buy_form",
                to="form.mandatory",
            ),
        ),
        migrations.AddField(
            model_name="shipment",
            name="buy_optional",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="optional_buy_form",
                to="form.optional",
            ),
        ),
        migrations.AddField(
            model_name="shipment",
            name="sell_mandatory",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="mandatory_sell_form",
                to="form.mandatory",
            ),
        ),
        migrations.AddField(
            model_name="shipment",
            name="sell_optional",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="optional_sell_form",
                to="form.optional",
            ),
        ),
        migrations.AlterField(
            model_name="baseform",
            name="AWB_no_first",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="AWB No First"
            ),
        ),
        migrations.AlterField(
            model_name="baseform",
            name="AWB_no_second",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="AWB No Second"
            ),
        ),
        migrations.AlterField(
            model_name="baseform",
            name="chargeable_weight",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Chargeable Weight"
            ),
        ),
        migrations.AlterField(
            model_name="baseform",
            name="gross_weight",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Gross Weight"
            ),
        ),
        migrations.AlterField(
            model_name="mandatory",
            name="airfreight",
            field=models.IntegerField(blank=True, null=True, verbose_name="Airfreight"),
        ),
        migrations.AlterField(
            model_name="mandatory",
            name="airway_bill",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Airway Bill"
            ),
        ),
        migrations.AlterField(
            model_name="mandatory",
            name="customs",
            field=models.IntegerField(blank=True, null=True, verbose_name="Customs "),
        ),
        migrations.AlterField(
            model_name="mandatory",
            name="other_charge",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Other Charge"
            ),
        ),
        migrations.AlterField(
            model_name="mandatory",
            name="pick_up",
            field=models.IntegerField(blank=True, null=True, verbose_name="Pick up"),
        ),
        migrations.AlterField(
            model_name="mandatory",
            name="sbl",
            field=models.IntegerField(blank=True, null=True, verbose_name="SBL"),
        ),
        migrations.AlterField(
            model_name="optional",
            name="airfreight",
            field=models.IntegerField(blank=True, null=True, verbose_name="Airfreight"),
        ),
        migrations.AlterField(
            model_name="optional",
            name="airway_bill",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Airway Bill"
            ),
        ),
        migrations.AlterField(
            model_name="optional",
            name="customs",
            field=models.IntegerField(blank=True, null=True, verbose_name="Customs "),
        ),
        migrations.AlterField(
            model_name="optional",
            name="document_under_our_compnay_name",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Document Under Our Compnay Name"
            ),
        ),
        migrations.AlterField(
            model_name="optional",
            name="ordino",
            field=models.IntegerField(blank=True, null=True, verbose_name="ordino"),
        ),
        migrations.AlterField(
            model_name="optional",
            name="other_charge",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Other Charge"
            ),
        ),
        migrations.AlterField(
            model_name="optional",
            name="pick_up",
            field=models.IntegerField(blank=True, null=True, verbose_name="Pick up"),
        ),
        migrations.AlterField(
            model_name="optional",
            name="warehouse_fee",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Warehouse Fee"
            ),
        ),
    ]
