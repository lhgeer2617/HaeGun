# Generated by Django 4.2.5 on 2023-10-06 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_rename_discription_article_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
