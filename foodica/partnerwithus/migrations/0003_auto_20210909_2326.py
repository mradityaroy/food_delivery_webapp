# Generated by Django 3.2.6 on 2021-09-09 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerwithus', '0002_fssai_customer_gstpan_own_bank_owner_info'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FSSAI_customer',
        ),
        migrations.DeleteModel(
            name='GSTPAN',
        ),
        migrations.DeleteModel(
            name='own_bank',
        ),
        migrations.DeleteModel(
            name='Owner_info',
        ),
        migrations.AddField(
            model_name='partner_with_us',
            name='acc_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='partner_with_us',
            name='bank_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='partner_with_us',
            name='branch_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='partner_with_us',
            name='fssai_exp_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='partner_with_us',
            name='fssai_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='partner_with_us',
            name='gst_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='partner_with_us',
            name='ifsc_code',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='partner_with_us',
            name='own_aadhar',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='partner_with_us',
            name='own_address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='partner_with_us',
            name='own_mobile',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='partner_with_us',
            name='own_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='partner_with_us',
            name='pan_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='partner_with_us',
            name='City',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='partner_with_us',
            name='Restaurant_Name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
