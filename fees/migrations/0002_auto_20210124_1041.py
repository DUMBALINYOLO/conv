# Generated by Django 3.1.4 on 2021-01-24 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20210124_1041'),
        ('fees', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentreceipt',
            name='cashier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='soldreceipts', to='people.bursarprofile'),
        ),
        migrations.AddField(
            model_name='studentreceipt',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receipts', to='people.studentprofile'),
        ),
        migrations.AddField(
            model_name='payment',
            name='bookkeeper',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='incoming_payments', to='people.bursarprofile'),
        ),
        migrations.AddField(
            model_name='payment',
            name='entry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.journalentry'),
        ),
        migrations.AddField(
            model_name='payment',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoicepayments', to='fees.invoice'),
        ),
        migrations.AddField(
            model_name='payment',
            name='receipt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payments', to='fees.studentreceipt'),
        ),
        migrations.AddField(
            model_name='invoiceline',
            name='fee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fees.fee'),
        ),
        migrations.AddField(
            model_name='invoiceline',
            name='invoice',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lines', to='fees.invoice'),
        ),
        migrations.AddField(
            model_name='invoiceline',
            name='tax',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.tax'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='bookkeeper',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoices', to='people.bursarprofile'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='entry',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.journalentry'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='student',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='myinvoices', to='people.studentprofile'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='validated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='people.bursarprofile'),
        ),
        migrations.AddField(
            model_name='feesconfig',
            name='tax',
            field=models.ForeignKey(blank='True', null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.tax'),
        ),
    ]
