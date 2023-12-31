# Generated by Django 4.2.7 on 2023-11-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.FileField(blank=True, null=True, upload_to='media')),
                ('discrpition', models.CharField(blank=True, max_length=200, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('feature_vector', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
