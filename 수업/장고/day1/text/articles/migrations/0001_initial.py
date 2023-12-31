# Generated by Django 4.2.5 on 2023-10-02 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.TextField()),
                ('pubdate', models.DateTimeField(auto_now=True)),
                ('price', models.IntegerField()),
                ('adult', models.BooleanField()),
            ],
        ),
    ]
