# Generated by Django 4.1.1 on 2022-10-29 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nsapp', '0003_searchmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterProjectLeaveList',
            fields=[
                ('leave_id', models.AutoField(db_column='Leave_ID', primary_key=True, serialize=False)),
                ('startdate', models.DateField(blank=True, db_column='Start_Date', null=True)),
                ('enddate', models.DateField(blank=True, db_column='End_Date', null=True)),
                ('remarks', models.TextField(blank=True, db_column='Remarks', null=True)),
            ],
            options={
                'db_table': 'Water_Project_Leave_List',
                'managed': False,
            },
        ),
    ]
