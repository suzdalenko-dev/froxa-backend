# Generated by Django 5.2.1 on 2025-06-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userfroxa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('password', models.TextField(null=True)),
                ('numvisit', models.TextField(null=True)),
                ('lastvisit', models.TextField(null=True)),
                ('role', models.TextField(null=True)),
                ('permissions', models.TextField(null=True)),
            ],
        ),
    ]
