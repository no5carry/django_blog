# Generated by Django 2.1.3 on 2018-12-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_them'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='them',
            field=models.CharField(choices=[('pc', 'Podcast'), ('lf', 'Life'), ('cw', 'CyberWorld')], default='cw', max_length=2),
        ),
    ]
