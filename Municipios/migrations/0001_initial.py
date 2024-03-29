# Generated by Django 4.0.1 on 2022-01-21 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('codigo', models.CharField(blank=True, max_length=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Linea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(blank=True, max_length=300, null=True)),
                ('mun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Municipios.municipio')),
            ],
        ),
    ]
