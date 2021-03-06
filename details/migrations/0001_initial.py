# Generated by Django 2.1.5 on 2019-01-11 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DashData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('name', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[(0, 'processing'), (1, 'success'), (2, 'queued'), (3, 'failed')], default='processing', max_length=20)),
                ('batch_id', models.DecimalField(decimal_places=0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('set_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('doc_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('name', models.TextField()),
                ('doc_status', models.CharField(choices=[(0, 'processing'), (1, 'success'), (2, 'queued'), (3, 'failed')], default='processing', max_length=20)),
                ('uploader', models.CharField(max_length=10)),
                ('date_uploaded', models.DateTimeField()),
            ],
        ),
    ]
