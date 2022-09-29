# Generated by Django 4.1.1 on 2022-09-27 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('engine', models.CharField(max_length=40, null=True)),
                ('hp', models.IntegerField(null=True)),
                ('nm', models.IntegerField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='model_image')),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='brands.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=50)),
                ('engine_s', models.CharField(max_length=40)),
                ('hp_s', models.IntegerField()),
                ('nm_s', models.IntegerField()),
                ('image_s', models.ImageField(blank=True, null=True, upload_to='series_image')),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.model')),
            ],
        ),
    ]
