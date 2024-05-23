# Generated by Django 5.0.6 on 2024-05-23 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('linkedin', models.JSONField(blank=True, null=True)),
                ('leetcode', models.JSONField(blank=True, null=True)),
                ('hackerrank', models.JSONField(blank=True, null=True)),
                ('gfg', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]