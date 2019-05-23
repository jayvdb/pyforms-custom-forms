# Generated by Django 2.2 on 2019-05-23 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formtypefields',
            name='field_parms',
            field=models.TextField(default=None, verbose_name='Parameters'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='formtypefields',
            name='field_type',
            field=models.CharField(choices=[('ControlText', 'Small text'), ('ControlCheckBox', 'Check box')], max_length=50, verbose_name='Field type'),
        ),
    ]
