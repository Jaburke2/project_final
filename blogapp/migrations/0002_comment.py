# Generated by Django 4.1.3 on 2022-12-02 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("name", models.CharField(max_length=225)),
                ("body", models.TextField()),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "post_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blogapp.post"
                    ),
                ),
            ],
        ),
    ]
