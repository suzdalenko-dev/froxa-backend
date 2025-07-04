# Generated by Django 5.2.1 on 2025-06-02 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0012_excelcalculations_delete_exceladditionalcalculations'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExcelCalculations',
        ),
        migrations.AddField(
            model_name='articlecostshead',
            name='aditivos',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='articlecostshead',
            name='amort_maq',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='articlecostshead',
            name='embalajes',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='articlecostshead',
            name='mod',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='articlecostshead',
            name='moi',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='articlecostshead',
            name='precio_aceite',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='articlecostshead',
            name='precio_materia_prima',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='articlecostshead',
            name='precio_servicios',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='articlecostshead',
            name='rendimiento',
            field=models.FloatField(null=True),
        ),
    ]
