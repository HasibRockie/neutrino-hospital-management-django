# Generated by Django 4.2.4 on 2023-09-02 15:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("doctors", "0003_alter_doctormodel_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="doctormodel",
            old_name="id",
            new_name="doctor_id",
        ),
    ]
