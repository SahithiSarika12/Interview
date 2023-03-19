# Generated by Django 3.0.8 on 2021-01-07 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adminlogin',
            fields=[
                ('Username', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=30)),
                ('Last_name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=50)),
                ('Gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10)),
                ('Date_of_birth', models.DateField(max_length=10)),
                ('Password', models.CharField(max_length=30)),
                ('Query', models.CharField(default='', max_length=3000)),
                ('Feedback', models.CharField(default='', max_length=3000)),
            ],
        ),
    ]