# Generated by Django 4.1.2 on 2023-02-06 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_index_bg_delete_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='DyfiUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=100)),
            ],
        ),
    ]
