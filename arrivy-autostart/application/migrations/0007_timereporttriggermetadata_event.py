# Generated by Django 4.2.4 on 2023-08-30 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_taskstatusdata_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeReportTriggerMetaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_status_id', models.IntegerField()),
                ('status_id', models.IntegerField()),
                ('task_id', models.IntegerField()),
                ('status_type', models.IntegerField()),
                ('status_title', models.CharField(max_length=255)),
                ('status_time', models.DateTimeField()),
                ('status_time_original_iso_str', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1000, 1000), (1001, 1001), (1002, 1002), (1003, 1003), (1004, 1004), (1005, 1005), (1006, 1006), (1007, 1007), (1008, 1008), (1009, 1009), (1051, 1051), (1053, 1053), (1052, 1052), (1100, 1100), (1101, 1101), (1102, 1102), (1103, 1103), (1200, 1200), (1201, 1201), (1202, 1202), (1203, 1203), (1204, 1204)], default=1001)),
                ('object_id', models.IntegerField()),
                ('object_type', models.IntegerField(choices=[(1000, 1000), (1001, 1001), (1002, 1002), (1003, 1003), (1004, 1004)], default=1001)),
                ('subject_id', models.IntegerField()),
                ('subject_type', models.IntegerField(choices=[(1000, 1000), (1001, 1001), (1002, 1002), (1003, 1003), (1004, 1004), (1100, 1100)], default=1001)),
                ('object_title', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('time', models.DateTimeField()),
                ('reporter_id', models.IntegerField()),
                ('reporter_name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.user')),
            ],
        ),
    ]
