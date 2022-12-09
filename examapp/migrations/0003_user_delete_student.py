# Generated by Django 4.0.6 on 2022-11-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0002_student_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('password1', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]