# Generated by Django 4.2 on 2023-05-05 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webGrupoCero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='obra',
            name='foto',
            field=models.ImageField(null=True, upload_to='foto'),
        ),
    ]