# Generated by Django 4.2 on 2023-05-18 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('breed', models.CharField(max_length=255)),
                ('species', models.CharField(max_length=255)),
                ('colour', models.CharField(max_length=255)),
                ('weight', models.IntegerField()),
                ('DOB', models.DateField()),
                ('vaccination_status', models.CharField(max_length=255)),
                ('microchip_number', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='owners.owner')),
            ],
        ),
    ]
