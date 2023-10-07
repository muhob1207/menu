# Generated by Django 4.2.1 on 2023-10-06 08:20

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ("menu_app", "0002_menuitem_menu_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menuitem",
            name="parent",
            field=mptt.fields.TreeForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="menu_app.menuitem",
            ),
        ),
    ]
