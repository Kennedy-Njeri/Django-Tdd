# Generated by Django 2.2.7 on 2020-01-02 12:19

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=main.models.recipe_image_file_path),
        ),
    ]
