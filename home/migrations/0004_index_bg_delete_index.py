# Generated by Django 4.1.2 on 2023-02-06 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_bloodgroup_gender_index_alter_contact_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index_bg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=50)),
                ('b_age', models.CharField(max_length=2)),
                ('b_donated', models.DateField()),
                ('b_gender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.gender')),
                ('b_group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.bloodgroup')),
            ],
        ),
        migrations.DeleteModel(
            name='Index',
        ),
    ]