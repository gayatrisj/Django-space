# Generated by Django 5.0.6 on 2024-05-21 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
