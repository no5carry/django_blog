# Generated by Django 2.1.3 on 2018-12-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20181128_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='them',
            field=models.CharField(choices=[('PC', 'Podcast'), ('LF', 'Life'), ('CW', 'CyberWorld')], default='CW', max_length=2),
        ),
    ]
