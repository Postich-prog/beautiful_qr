# Generated by Django 2.2.19 on 2023-11-07 08:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("qr_code", "0005_auto_20231107_1118"),
    ]

    operations = [
        migrations.AddField(
            model_name="qr",
            name="qurl",
            field=models.TextField(blank=True, verbose_name="Путь к коду"),
        ),
    ]
