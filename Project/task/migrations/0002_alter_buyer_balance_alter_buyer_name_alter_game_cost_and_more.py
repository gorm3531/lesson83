# Generated by Django 5.1.3 on 2024-11-20 10:55

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='game',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='game',
            name='size',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
