# Generated by Django 2.2 on 2019-05-23 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_forms', '0013_auto_20190523_1837'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='fieldvalue',
            unique_together={('formtype_field', 'formtype_object')},
        ),
    ]
