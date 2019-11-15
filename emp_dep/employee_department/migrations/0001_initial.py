# Generated by Django 2.1 on 2019-11-14 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('d_id', models.IntegerField(primary_key=True, serialize=False)),
                ('d_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('e_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('contact', models.IntegerField()),
                ('salary', models.FloatField()),
                ('role', models.CharField(max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_department.Department')),
            ],
        ),
    ]
