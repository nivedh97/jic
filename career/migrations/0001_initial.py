# Generated by Django 4.0.2 on 2022-02-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Career Name', max_length=50)),
                ('experience', models.CharField(help_text='Career Name', max_length=50)),
                ('Details', models.CharField(max_length=1000)),
            ],
        ),
    ]
