# Generated by Django 3.1.3 on 2020-12-13 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_auto_20201213_2106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='name',
            new_name='names',
        ),
    ]