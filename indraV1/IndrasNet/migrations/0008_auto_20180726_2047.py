# Generated by Django 2.0.7 on 2018-07-26 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IndrasNet', '0007_merge_20180726_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='disp_name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='modelparam',
            name='default_val',
            field=models.CharField(blank=True, default='', max_length=16, null=True),
        ),
    ]