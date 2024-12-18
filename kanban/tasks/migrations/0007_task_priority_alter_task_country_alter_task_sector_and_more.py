# Generated by Django 4.2.6 on 2024-11-29 10:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0006_rename_column_status_task_column"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="priority",
            field=models.CharField(
                choices=[("high", "High"), ("medium", "Medium"), ("low", "Low")],
                default="medium",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="country",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="task",
            name="sector",
            field=models.CharField(
                blank=True,
                choices=[
                    ("aardappelen", "Aardappelen"),
                    ("bloembollen", "Bloembollen"),
                    ("divers", "Diverse Producten"),
                    ("groenteenfruit", "Groente en Fruit"),
                    ("plantuien", "Plantuien, Sjalotten, Knoflook"),
                    ("sierteelt", "Sierteelt, Boomkwekerij en Fruitgewassen"),
                    ("zaaizaden", "Zaaizaden"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="status",
            field=models.CharField(
                choices=[("todo", "To Do"), ("doing", "Doing"), ("waiting", "Waiting")],
                default="todo",
                max_length=10,
            ),
        ),
    ]
