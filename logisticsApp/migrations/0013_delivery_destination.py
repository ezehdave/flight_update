# Generated by Django 4.1.6 on 2023-03-10 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logisticsApp', '0012_crypto_payment_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery_destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('status', models.BooleanField(default=False, null=True)),
            ],
        ),
    ]