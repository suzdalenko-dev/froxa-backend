# Generated by Django 5.2.1 on 2025-06-12 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0021_rename_equivalentsheades_equivalentshead'),
    ]

    operations = [
        migrations.AddField(
            model_name='excellineseditable',
            name='precio_padre_mas_gastos',
            field=models.FloatField(null=True),
        ),
    ]
