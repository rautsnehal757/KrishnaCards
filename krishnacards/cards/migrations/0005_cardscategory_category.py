# Generated by Django 3.1.7 on 2023-07-18 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_cardscategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardscategory',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cards.categories'),
        ),
    ]
