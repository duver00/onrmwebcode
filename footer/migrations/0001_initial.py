# Generated by Django 3.2.5 on 2021-09-23 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ControlInterno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('documento', models.FileField(upload_to='control')),
            ],
            options={
                'verbose_name': 'Control Interno',
            },
        ),
        migrations.CreateModel(
            name='DocumentosRectores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('documento', models.FileField(upload_to='rectores')),
            ],
        ),
        migrations.CreateModel(
            name='LinksExternos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('url', models.URLField()),
            ],
        ),
    ]
