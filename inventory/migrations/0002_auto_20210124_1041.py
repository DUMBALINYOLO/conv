# Generated by Django 3.1.4 on 2021-01-24 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20210124_1041'),
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='inventory_controller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.bursarprofile'),
        ),
        migrations.AddField(
            model_name='transferorderline',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.inventoryitem'),
        ),
        migrations.AddField(
            model_name='transferorderline',
            name='transfer_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lines', to='inventory.transferorder'),
        ),
        migrations.AddField(
            model_name='transferorder',
            name='issuing_inventory_controller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issuing_inventory_controller', to='people.bursarprofile'),
        ),
        migrations.AddField(
            model_name='transferorder',
            name='receiving_inventory_controller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.bursarprofile'),
        ),
        migrations.AddField(
            model_name='transferorder',
            name='receiving_warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.warehouse'),
        ),
        migrations.AddField(
            model_name='transferorder',
            name='source_warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='source_warehouse', to='inventory.warehouse'),
        ),
        migrations.AddField(
            model_name='supplieraddress',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='addresses', to='inventory.supplier'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.account'),
        ),
        migrations.AddField(
            model_name='storagemedia',
            name='warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='storagemedias', to='inventory.warehouse'),
        ),
        migrations.AddField(
            model_name='stockreceiptline',
            name='line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.orderitem'),
        ),
        migrations.AddField(
            model_name='stockreceiptline',
            name='receipt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lines', to='inventory.stockreceipt'),
        ),
        migrations.AddField(
            model_name='stockreceipt',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.order'),
        ),
        migrations.AddField(
            model_name='stockreceipt',
            name='received_by',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.bursarprofile'),
        ),
        migrations.AddField(
            model_name='stockadjustment',
            name='inventory_check',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adjustments', to='inventory.inventorycheck'),
        ),
        migrations.AddField(
            model_name='stockadjustment',
            name='warehouse_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.inventorystockitem'),
        ),
        migrations.AddField(
            model_name='orderpayment',
            name='entry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.journalentry'),
        ),
        migrations.AddField(
            model_name='orderpayment',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.order'),
        ),
        migrations.AddField(
            model_name='orderpayment',
            name='paid_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orderpayments', to='people.bursarprofile'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.inventoryitem'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='inventory.order'),
        ),
        migrations.AddField(
            model_name='order',
            name='entry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_entry', to='accounts.journalentry'),
        ),
        migrations.AddField(
            model_name='order',
            name='issuing_inventory_controller',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='people.bursarprofile'),
        ),
        migrations.AddField(
            model_name='order',
            name='ship_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.warehouse'),
        ),
        migrations.AddField(
            model_name='order',
            name='supplier',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.supplier'),
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.tax'),
        ),
        migrations.AddField(
            model_name='order',
            name='validated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.bursarprofile'),
        ),
        migrations.AddField(
            model_name='inventorystockitem',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.inventoryitem'),
        ),
        migrations.AddField(
            model_name='inventorystockitem',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inventoryitems', to='inventory.storagemedia'),
        ),
        migrations.AddField(
            model_name='inventorystockitem',
            name='warehouse',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inventorystockitems', to='inventory.warehouse'),
        ),
        migrations.AddField(
            model_name='inventoryscrappingrecordline',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.inventoryitem'),
        ),
        migrations.AddField(
            model_name='inventoryscrappingrecordline',
            name='scrapping_record',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lines', to='inventory.inventoryscrappingrecord'),
        ),
        migrations.AddField(
            model_name='inventoryscrappingrecord',
            name='controller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.bursarprofile'),
        ),
        migrations.AddField(
            model_name='inventoryscrappingrecord',
            name='warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.warehouse'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='category',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.category'),
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.supplier'),
        ),
        migrations.AddField(
            model_name='inventorycheck',
            name='adjusted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.bursarprofile'),
        ),
        migrations.AddField(
            model_name='inventorycheck',
            name='warehouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.warehouse'),
        ),
        migrations.AddField(
            model_name='historicalstockreceiptline',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalstockreceiptline',
            name='line',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='inventory.orderitem'),
        ),
        migrations.AddField(
            model_name='historicalstockreceiptline',
            name='receipt',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='inventory.stockreceipt'),
        ),
        migrations.AddField(
            model_name='historicalstockreceipt',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalstockreceipt',
            name='order',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='inventory.order'),
        ),
        migrations.AddField(
            model_name='historicalstockreceipt',
            name='received_by',
            field=models.ForeignKey(blank=True, db_constraint=False, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='people.bursarprofile'),
        ),
        migrations.AddField(
            model_name='historicalstockadjustment',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalstockadjustment',
            name='inventory_check',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='inventory.inventorycheck'),
        ),
        migrations.AddField(
            model_name='historicalstockadjustment',
            name='warehouse_item',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='inventory.inventorystockitem'),
        ),
        migrations.AddField(
            model_name='historicalorderpayment',
            name='entry',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='accounts.journalentry'),
        ),
        migrations.AddField(
            model_name='historicalorderpayment',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalorderpayment',
            name='order',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='inventory.order'),
        ),
        migrations.AddField(
            model_name='historicalorderpayment',
            name='paid_by',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='people.bursarprofile'),
        ),
        migrations.AddField(
            model_name='historicalinventorycheck',
            name='adjusted_by',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='people.bursarprofile'),
        ),
        migrations.AddField(
            model_name='historicalinventorycheck',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalinventorycheck',
            name='warehouse',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='inventory.warehouse'),
        ),
        migrations.AddField(
            model_name='debitnoteline',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.orderitem'),
        ),
        migrations.AddField(
            model_name='debitnoteline',
            name='note',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lines', to='inventory.debitnote'),
        ),
        migrations.AddField(
            model_name='debitnote',
            name='entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.journalentry'),
        ),
        migrations.AddField(
            model_name='debitnote',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.order'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.category'),
        ),
    ]