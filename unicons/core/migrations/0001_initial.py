# Generated by Django 3.2.9 on 2021-12-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelUploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_name', models.CharField(blank=True, max_length=255, null=True)),
                ('recovery_file', models.FileField(upload_to='recovery_files')),
            ],
        ),
    ]