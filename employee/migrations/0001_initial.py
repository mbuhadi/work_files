# Generated by Django 4.2.4 on 2023-08-15 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=60)),
                ('name_ar', models.CharField(max_length=60)),
                ('file_id', models.CharField(max_length=60)),
                ('finger_print_id', models.CharField(max_length=60)),
                ('department', models.CharField(max_length=60)),
                ('national_id', models.CharField(max_length=60)),
            ],
        ),
    ]
