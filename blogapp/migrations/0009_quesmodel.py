# Generated by Django 4.1.3 on 2022-12-03 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0008_flex_video"),
    ]

    operations = [
        migrations.CreateModel(
            name="QuesModel",
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
                ("question", models.CharField(max_length=200, null=True)),
                ("op1", models.CharField(max_length=200, null=True)),
                ("op2", models.CharField(max_length=200, null=True)),
                ("op3", models.CharField(max_length=200, null=True)),
                ("op4", models.CharField(max_length=200, null=True)),
                ("ans", models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
