# Generated by Django 4.2.5 on 2024-06-08 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breweries', '0003_alter_brewery_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewery',
            name='id',
            field=models.UUIDField(default='c566ea55-026f-4949-8ede-0b7c6320cbaf', editable=False, primary_key=True, serialize=False),
        ),
    ]
