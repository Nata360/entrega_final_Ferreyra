# Generated by Django 4.2.3 on 2023-08-07 23:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoextra',
            name='biografia',
            field=ckeditor.fields.RichTextField(blank=True, max_length=500, null=True),
        ),
    ]
