# Generated by Django 2.2.3 on 2019-09-09 20:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmonitor', '0002_auto_20190909_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billboard',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 23, 22, 11, 958453)),
        ),
        migrations.AlterField(
            model_name='billboard',
            name='lastUpdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 23, 22, 11, 974082)),
        ),
        migrations.AlterField(
            model_name='billboard',
            name='latittude',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=30),
        ),
        migrations.AlterField(
            model_name='billboard',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=30),
        ),
        migrations.AlterField(
            model_name='billboardbrand',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 23, 22, 11, 974082)),
        ),
        migrations.AlterField(
            model_name='billboardbrand',
            name='lastUpdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 23, 22, 11, 974082)),
        ),
        migrations.AlterField(
            model_name='boardsupplier',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 9, 23, 22, 11, 974082)),
        ),
        migrations.AlterField(
            model_name='brand',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 23, 22, 11, 958453)),
        ),
        migrations.AlterField(
            model_name='brand',
            name='lastUpdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 23, 22, 11, 958453)),
        ),
        migrations.AlterField(
            model_name='brandagency',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 23, 22, 11, 958453)),
        ),
        migrations.AlterField(
            model_name='brandagency',
            name='lastUpdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 23, 22, 11, 958453)),
        ),
        migrations.AlterField(
            model_name='client',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 23, 22, 11, 958453)),
        ),
        migrations.AlterField(
            model_name='client',
            name='lastUpdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 23, 22, 11, 958453)),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 23, 22, 11, 974082)),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='lastUpdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 23, 22, 11, 974082)),
        ),
        migrations.AlterField(
            model_name='image',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 23, 22, 11, 974082)),
        ),
        migrations.AlterField(
            model_name='mediaagency',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 23, 22, 11, 958453)),
        ),
        migrations.AlterField(
            model_name='mediaagency',
            name='lastUpdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 23, 22, 11, 958453)),
        ),
        migrations.AlterField(
            model_name='town',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 23, 22, 11, 958453)),
        ),
        migrations.AlterField(
            model_name='users',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 23, 22, 11, 974082)),
        ),
        migrations.AlterField(
            model_name='users',
            name='lastUpdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 9, 23, 22, 11, 974082)),
        ),
    ]
