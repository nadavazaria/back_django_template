# Generated by Django 5.0.2 on 2024-02-20 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
