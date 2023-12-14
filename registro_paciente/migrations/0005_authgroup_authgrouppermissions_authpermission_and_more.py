# Generated by Django 4.2.5 on 2023-11-02 09:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registro_paciente", "0004_pruebasmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthGroup",
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
                ("name", models.CharField(max_length=150, unique=True)),
            ],
            options={
                "db_table": "auth_group",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthGroupPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_group_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthPermission",
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
                ("name", models.CharField(max_length=255)),
                ("codename", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "auth_permission",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUser",
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
                ("password", models.CharField(max_length=128)),
                ("last_login", models.DateTimeField(blank=True, null=True)),
                ("is_superuser", models.BooleanField()),
                ("username", models.CharField(max_length=150, unique=True)),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(max_length=150)),
                ("email", models.CharField(max_length=254)),
                ("is_staff", models.BooleanField()),
                ("is_active", models.BooleanField()),
                ("date_joined", models.DateTimeField()),
            ],
            options={
                "db_table": "auth_user",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserGroups",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_user_groups",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="AuthUserUserPermissions",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "auth_user_user_permissions",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoAdminLog",
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
                ("action_time", models.DateTimeField()),
                ("object_id", models.TextField(blank=True, null=True)),
                ("object_repr", models.CharField(max_length=200)),
                ("action_flag", models.SmallIntegerField()),
                ("change_message", models.TextField()),
            ],
            options={
                "db_table": "django_admin_log",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoContentType",
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
                ("app_label", models.CharField(max_length=100)),
                ("model", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "django_content_type",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoMigrations",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("app", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("applied", models.DateTimeField()),
            ],
            options={
                "db_table": "django_migrations",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="DjangoSession",
            fields=[
                (
                    "session_key",
                    models.CharField(max_length=40, primary_key=True, serialize=False),
                ),
                ("session_data", models.TextField()),
                ("expire_date", models.DateTimeField()),
            ],
            options={
                "db_table": "django_session",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Estudio",
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
                ("id_estudio", models.CharField(max_length=11)),
                ("prueba", models.CharField(max_length=255)),
                ("entrega", models.CharField(max_length=15)),
                ("estudios_extras", models.CharField(max_length=255)),
                ("muestra", models.CharField(max_length=255)),
                ("metodo", models.CharField(max_length=255)),
                ("observacion", models.CharField(max_length=255)),
                ("costo", models.IntegerField()),
                ("tipo_e", models.CharField(max_length=15)),
            ],
            options={
                "db_table": "estudio",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Estudios",
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
                ("id_estudio", models.IntegerField(blank=True, null=True)),
                ("prueba", models.CharField(max_length=255)),
                ("entrega", models.CharField(max_length=15)),
                ("estudios_extras", models.CharField(max_length=255)),
                ("muestra", models.CharField(max_length=255)),
                ("metodo", models.CharField(max_length=255)),
                ("observacion", models.CharField(max_length=255)),
                ("costo", models.IntegerField()),
                ("tipo_e", models.CharField(max_length=15)),
            ],
            options={
                "db_table": "estudios",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Pruebas",
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
                ("nombre", models.CharField(blank=True, null=True)),
                ("costo", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "pruebas",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="RegistroPacientePruebasmodel",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "registro_paciente_pruebasmodel",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="RegistroPacienteRegistro",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("prueba", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "registro_paciente_registro",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="RegistroPacienteRegistrodosmodel",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("nombre", models.CharField(max_length=200)),
                ("apellido_paterno", models.CharField(max_length=200)),
                ("apellido_materno", models.CharField(max_length=200)),
                ("genero", models.CharField(max_length=200)),
                ("telefono", models.CharField(max_length=200)),
                ("edad", models.CharField(max_length=200)),
                ("prueba", models.CharField(max_length=200)),
                ("diagnostico", models.CharField(max_length=200)),
                ("doctor", models.CharField(max_length=200)),
                ("fecha", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "registro_paciente_registrodosmodel",
                "managed": False,
            },
        ),
        migrations.DeleteModel(
            name="pruebasModel",
        ),
        migrations.DeleteModel(
            name="RegistroDosModel",
        ),
        migrations.AlterModelOptions(
            name="registro",
            options={"managed": False},
        ),
    ]
