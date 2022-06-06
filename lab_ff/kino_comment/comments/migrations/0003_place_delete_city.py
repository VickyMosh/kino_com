# Generated by Django 4.0.4 on 2022-06-06 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'places',
            },
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
