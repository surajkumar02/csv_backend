# Generated by Django 4.0 on 2022-03-29 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_f_name', models.CharField(max_length=100)),
                ('student_m_name', models.CharField(max_length=100)),
                ('student_l_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Others', 'others')], max_length=10)),
                ('student_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.city')),
                ('student_state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.state')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.state'),
        ),
    ]
