# Generated by Django 2.2.19 on 2023-11-07 08:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("qr_code", "0004_auto_20231107_0003"),
    ]

    operations = [
        migrations.AlterField(
            model_name="qr",
            name="image",
            field=models.ImageField(upload_to="", verbose_name="Картинка"),
        ),
    ]
