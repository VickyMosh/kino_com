# Generated by Django 4.0.5 on 2022-06-07 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0006_alter_comment_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.CharField(max_length=30)),
                ('text', models.TextField(verbose_name='текст предложения')),
            ],
        ),
    ]
