# Generated by Django 4.2.5 on 2023-10-30 16:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registro_paciente", "0003_rename_registrodos_registrodosmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="pruebasModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=200)),
            ],
        ),
    ]