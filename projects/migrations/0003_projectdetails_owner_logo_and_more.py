# Generated by Django 4.0.2 on 2022-02-06 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_proectdetails_projectdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdetails',
            name='owner_logo',
            field=models.ImageField(null=True, upload_to='uploads/project/'),
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='project_image',
            field=models.ImageField(null=True, upload_to='uploads/project/'),
        ),
        migrations.AlterField(
            model_name='projectdetails',
            name='owned_by',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='projectdetails',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
