# Generated by Django 4.2.1 on 2023-10-06 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "menu_app",
            "0005_rename_name_menuitem_title_remove_menuitem_named_url_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="menuitem",
            old_name="title",
            new_name="name",
        ),
        migrations.RemoveField(
            model_name="menuitem",
            name="menu_name",
        ),
    ]