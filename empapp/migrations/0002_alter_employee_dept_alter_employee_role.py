# Generated by Django 5.0.6 on 2024-07-04 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("empapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="dept",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="dept",
                to="empapp.department",
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="role",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="role",
                to="empapp.role",
            ),
        ),
    ]
