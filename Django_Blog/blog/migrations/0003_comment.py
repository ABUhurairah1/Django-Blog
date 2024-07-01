# Generated by Django 5.0.2 on 2024-07-01 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_host_alter_blog_description_alter_blog_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, default='', null=True)),
                ('blog', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
    ]