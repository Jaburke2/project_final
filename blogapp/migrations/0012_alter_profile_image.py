# Generated by Django 4.1.3 on 2022-12-04 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0011_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                default="https://res.cloudinary.com/dxzsuwkr7/image/upload/v1670110715/blog-post-image/default_yjw8rs.png",
                upload_to="blog-post-image",
            ),
        ),
    ]
