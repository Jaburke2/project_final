# Generated by Django 4.1.3 on 2022-12-06 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0015_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                default="https://res.cloudinary.com/dxzsuwkr7/image/upload/v1670295320/blog-post-image/what_gzzgu5.png",
                upload_to="",
            ),
        ),
    ]