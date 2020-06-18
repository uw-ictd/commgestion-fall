# Generated by Django 3.0.7 on 2020-06-11 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20200310_0439'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackhaulUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('up_kbytes', models.FloatField()),
                ('down_kbytes', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='HostUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=255, unique=True)),
                ('timestamp', models.DateTimeField()),
                ('up_kbytes', models.FloatField()),
                ('down_kbytes', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RanUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('up_kbytes', models.FloatField()),
                ('down_kbytes', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SubscriberUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('up_kbytes', models.FloatField()),
                ('down_kbytes', models.FloatField()),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Subscriber')),
            ],
        ),
        migrations.DeleteModel(
            name='Application',
        ),
        migrations.DeleteModel(
            name='Usage',
        ),
    ]