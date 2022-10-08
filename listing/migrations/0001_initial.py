# Generated by Django 4.1 on 2022-09-08 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category_of_List",
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
                ("name", models.CharField(max_length=15)),
            ],
            options={"verbose_name": "Category", "verbose_name_plural": "Categories",},
        ),
        migrations.CreateModel(
            name="Listing",
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
                ("title", models.CharField(max_length=200)),
                ("created_time_stamp", models.DateTimeField(default="2022-09-08")),
                ("description", models.TextField(blank=True)),
                ("due_date", models.DateTimeField(default="2022-09-08")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="listing.category_of_list",
                    ),
                ),
            ],
            options={"ordering": ["due_date"],},
        ),
    ]
