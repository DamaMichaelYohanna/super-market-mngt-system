# Generated by Django 3.1.6 on 2021-03-21 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smms', '0008_auto_20210208_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='ref_id',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
