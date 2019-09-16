# Generated by Django 2.2.3 on 2019-09-13 14:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bmonitor', '0004_auto_20190913_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billboard',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 13, 17, 49, 18, 962078)),
        ),
        migrations.AlterField(
            model_name='billboard',
            name='lastUpdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 13, 17, 49, 18, 962078)),
        ),
        migrations.AlterField(
            model_name='billboardbrand',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 13, 17, 49, 18, 962078)),
        ),
        migrations.AlterField(
            model_name='billboardbrand',
            name='lastUpdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 13, 17, 49, 18, 962078)),
        ),
        migrations.AlterField(
            model_name='boardsupplier',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 13, 17, 49, 18, 965075)),
        ),
        migrations.AlterField(
            model_name='brand',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 13, 17, 49, 18, 961077)),
        ),
        migrations.AlterField(
            model_name='brand',
            name='lastUpdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 13, 17, 49, 18, 961077)),
        ),
        migrations.AlterField(
            model_name='brandagency',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 13, 17, 49, 18, 961077)),
        ),
        migrations.AlterField(
            model_name='brandagency',
            name='lastUpdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 13, 17, 49, 18, 961077)),
        ),
        migrations.AlterField(
            model_name='client',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 13, 17, 49, 18, 960078)),
        ),
        migrations.AlterField(
            model_name='client',
            name='lastUpdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 13, 17, 49, 18, 960078)),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 13, 17, 49, 18, 964076)),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='lastUpdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 13, 17, 49, 18, 964076)),
        ),
        migrations.AlterField(
            model_name='image',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 13, 17, 49, 18, 963077)),
        ),
        migrations.AlterField(
            model_name='mediaagency',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 13, 17, 49, 18, 959079)),
        ),
        migrations.AlterField(
            model_name='mediaagency',
            name='lastUpdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 13, 17, 49, 18, 959079)),
        ),
        migrations.AlterField(
            model_name='town',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 13, 17, 49, 18, 959079)),
        ),
        migrations.AlterField(
            model_name='users',
            name='agency',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='bmonitor.MediaAgency'),
        ),
        migrations.AlterField(
            model_name='users',
            name='client',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='bmonitor.Client'),
        ),
        migrations.AlterField(
            model_name='users',
            name='dateCreated',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 13, 17, 49, 18, 964076)),
        ),
        migrations.AlterField(
            model_name='users',
            name='lastUpdate',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 13, 17, 49, 18, 964076)),
        ),
    ]