# Generated by Django 4.2.5 on 2023-12-12 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Doctor",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("contact_number", models.CharField(max_length=15)),
                ("address", models.TextField()),
                ("speciality", models.CharField(max_length=100)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={"db_table": "doctor",},
        ),
        migrations.CreateModel(
            name="Patient",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("contact_number", models.CharField(max_length=15)),
                ("date_of_birth", models.DateField()),
                ("address", models.TextField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
            options={"db_table": "patient",},
        ),
        migrations.CreateModel(
            name="PatientAppointment",
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
                ("appointment_time", models.DateTimeField()),
                ("status", models.CharField(default="Scheduled", max_length=100)),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web_app.doctor"
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="web_app.patient",
                    ),
                ),
            ],
            options={"db_table": "patient_appointment",},
        ),
        migrations.CreateModel(
            name="DoctorAppointment",
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
                ("appointment_time", models.DateTimeField()),
                ("status", models.CharField(default="Scheduled", max_length=100)),
                ("notes", models.TextField(blank=True, null=True)),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="web_app.doctor"
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="web_app.patient",
                    ),
                ),
            ],
            options={"db_table": "doctor_appointment",},
        ),
    ]
