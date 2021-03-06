# Generated by Django 3.1.4 on 2020-12-18 17:09

from django.db import migrations, models
import django.db.models.deletion
import ledger.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer_id', models.IntegerField(default=0)),
                ('preferred_name', models.CharField(blank=True, max_length=255)),
                ('full_name', models.CharField(blank=True, max_length=255)),
                ('profile_pic', models.ImageField(upload_to=ledger.models.get_filename)),
            ],
        ),
        migrations.CreateModel(
            name='Savings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('remark', models.CharField(max_length=600)),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ledger.month')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('remark', models.CharField(max_length=600)),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ledger.month')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(default=0)),
                ('remark', models.CharField(max_length=600)),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ledger.month')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('number', models.CharField(blank=True, max_length=255)),
                ('order', models.IntegerField(default=0)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='ledger.person')),
            ],
        ),
    ]
