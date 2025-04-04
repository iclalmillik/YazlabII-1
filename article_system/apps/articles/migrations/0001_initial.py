# Generated by Django 5.1.7 on 2025-03-18 12:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('pdf_file', models.FileField(upload_to='articles/')),
                ('author_email', models.EmailField(max_length=254)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('review_status', models.CharField(default='Pending', max_length=20)),
                ('tracking_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
        ),
    ]
