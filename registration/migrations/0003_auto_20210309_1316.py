# Generated by Django 3.1.6 on 2021-03-09 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
        ('registration', '0002_delete_systemuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprovider',
            name='cat_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='service.category'),
        ),
    ]