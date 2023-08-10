# Generated by Django 3.1.7 on 2023-07-17 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20230717_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('urls', models.CharField(max_length=100)),
            ],
        ),
    ]
