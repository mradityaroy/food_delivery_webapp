# Generated by Django 3.2.6 on 2021-09-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerwithus', '0004_auto_20210910_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner_with_us',
            name='aadhar_file',
            field=models.CharField(max_length=50, null=True),
        ),
    ]