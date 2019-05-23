# Generated by Django 2.2 on 2019-05-23 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('custom_forms', '0010_auto_20190523_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormTypeObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(verbose_name='Object id')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('form_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_forms.FormType')),
            ],
        ),
        migrations.CreateModel(
            name='FieldValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(verbose_name='Value')),
                ('formtype_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_forms.FormTypeField')),
                ('formtype_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_forms.FormTypeObject')),
            ],
        ),
    ]
