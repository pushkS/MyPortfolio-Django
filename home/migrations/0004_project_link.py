# Generated by Django 3.1.4 on 2021-03-21 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210321_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
    ]
