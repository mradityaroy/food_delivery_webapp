# Generated by Django 3.2.6 on 2021-09-15 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerwithus', '0009_auto_20210912_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner_with_us',
            name='aadhar_file',
            field=models.FileField(null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='partner_with_us',
            name='gst_file',
            field=models.FileField(null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='partner_with_us',
            name='img_file',
            field=models.FileField(null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='partner_with_us',
            name='menu_file',
            field=models.FileField(null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='partner_with_us',
            name='pan_file',
            field=models.FileField(null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='partner_with_us',
            name='sign_file',
            field=models.FileField(null=True, upload_to='media/'),
        ),
    ]
