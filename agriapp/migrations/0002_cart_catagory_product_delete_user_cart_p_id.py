# Generated by Django 5.0.2 on 2024-03-14 09:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("agriapp", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cart",
            fields=[
                ("cid", models.AutoField(primary_key=True, serialize=False)),
                ("quantity", models.IntegerField()),
                (
                    "u_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Catagory",
            fields=[
                ("cid", models.AutoField(primary_key=True, serialize=False)),
                ("cname", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("pid", models.AutoField(primary_key=True, serialize=False)),
                ("pname", models.CharField(max_length=30)),
                ("pprice", models.IntegerField()),
                ("pdesc", models.TextField()),
                ("pimg", models.ImageField(upload_to="pro_images/")),
                (
                    "c_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="agriapp.catagory",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="User",
        ),
        migrations.AddField(
            model_name="cart",
            name="p_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="agriapp.product"
            ),
        ),
    ]