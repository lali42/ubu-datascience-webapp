# Generated by Django 2.2.7 on 2020-01-15 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('sepal_length', models.IntegerField()),
                ('sepal_width', models.IntegerField()),
                ('petal_length', models.IntegerField()),
                ('petal_width', models.IntegerField()),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='irisapp.Species')),
            ],
        ),
    ]
