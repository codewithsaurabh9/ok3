# Generated by Django 4.2.4 on 2023-08-23 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0002_about_freelance_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutproject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Freelance_project', models.CharField(blank=True, max_length=150)),
                ('Freelance_num', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]
